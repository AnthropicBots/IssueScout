"""
Reusable OpenAPI response definitions.
"""

from issuescout.api.v1.docs.examples import (
    REPOSITORY_EXAMPLE,
    SCAN_JOB_CREATED_EXAMPLE,
    SCAN_JOB_STATS_EXAMPLE,
)

REPOSITORY_RESPONSES = {
    200: {
        "description": "Repository information retrieved successfully.",
        "content": {
            "application/json": {
                "example": REPOSITORY_EXAMPLE,
            },
        },
    },
}

SCAN_JOB_CREATE_RESPONSES = {
    200: {
        "description": "Scan job created successfully.",
        "content": {
            "application/json": {
                "example": SCAN_JOB_CREATED_EXAMPLE,
            },
        },
    },
}

SCAN_JOB_STATS_RESPONSES = {
    200: {
        "description": "Scan job statistics.",
        "content": {
            "application/json": {
                "example": SCAN_JOB_STATS_EXAMPLE,
            },
        },
    },
}
