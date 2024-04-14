from loguru import logger

from aero_copilot.core.settings import settings

if not settings.log.path.parent.exists():
    settings.log.path.parent.mkdir(parents=True)

logger.add(
    settings.log.path,
    level=settings.log.level,
    rotation=settings.log.rotation,
    serialize=settings.log.serialize,
)
