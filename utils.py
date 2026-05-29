"""Utility functions for input validation and formatting."""
import re
from datetime import datetime


def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_username(username: str) -> tuple[bool, str]:
    """
    Validate username: 3-20 chars, alphanumeric + underscore only.
    Returns (is_valid, error_message).
    """
    if not username:
        return False, "Username cannot be empty"
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    if len(username) > 20:
        return False, "Username must be at most 20 characters"
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores"
    return True, ""


def format_datetime(dt: datetime) -> str:
    """Format datetime to ISO 8601 string."""
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


def paginate(items: list, page: int, page_size: int = 20) -> dict:
    """Return paginated slice with metadata."""
    if page < 1:
        page = 1
    total = len(items)
    total_pages = (total + page_size - 1) // page_size
    start = (page - 1) * page_size
    end = start + page_size
    return {
        'items': items[start:end],
        'page': page,
        'page_size': page_size,
        'total': total,
        'total_pages': total_pages,
        'has_next': page < total_pages,
        'has_prev': page > 1,
    }
