import logging

import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.conf import settings

logger = logging.getLogger(__name__)


def is_cloudinary_configured():
    """Check if Cloudinary settings are available and enabled."""
    return (
        getattr(settings, 'USE_CLOUDINARY', False)
        and getattr(settings, 'CLOUDINARY_CLOUD_NAME', '')
        and getattr(settings, 'CLOUDINARY_API_KEY', '')
        and getattr(settings, 'CLOUDINARY_API_SECRET', '')
    )


def configure_cloudinary():
    """Configure the Cloudinary SDK from Django settings."""
    if is_cloudinary_configured():
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_CLOUD_NAME,
            api_key=settings.CLOUDINARY_API_KEY,
            api_secret=settings.CLOUDINARY_API_SECRET,
            secure=True,
        )


def upload_to_cloudinary(file_obj, public_id):
    """Upload a file to Cloudinary. Returns the public_id on success, None on failure."""
    if not is_cloudinary_configured():
        return None
    try:
        configure_cloudinary()
        result = cloudinary.uploader.upload(
            file_obj,
            public_id=public_id,
            resource_type='image',
            overwrite=True,
        )
        return result.get('public_id')
    except Exception as e:
        logger.error('Cloudinary upload failed: %s', e)
        return None


def get_cloudinary_url(public_id):
    """Get the URL for a Cloudinary image."""
    if not public_id:
        return None
    try:
        configure_cloudinary()
        url, _ = cloudinary.utils.cloudinary_url(public_id, secure=True)
        return url
    except Exception as e:
        logger.error('Cloudinary URL generation failed: %s', e)
        return None


def delete_from_cloudinary(public_id):
    """Delete an image from Cloudinary."""
    if not is_cloudinary_configured() or not public_id:
        return
    try:
        configure_cloudinary()
        cloudinary.uploader.destroy(public_id, resource_type='image')
    except Exception as e:
        logger.error('Cloudinary delete failed: %s', e)


def delete_folder_from_cloudinary(prefix):
    """Delete all images with a given prefix from Cloudinary."""
    if not is_cloudinary_configured() or not prefix:
        return
    try:
        configure_cloudinary()
        cloudinary.api.delete_resources_by_prefix(prefix, resource_type='image')
    except Exception as e:
        logger.error('Cloudinary folder delete failed: %s', e)
