from .start import register_start_handlers
from .model import register_model_handlers
from .platform import register_platform_handlers
from .media import register_media_handlers
from .survey import register_survey_handlers

def register_handlers(bot):
    register_start_handlers(bot)
    register_model_handlers(bot)
    register_platform_handlers(bot)
    register_media_handlers(bot)
    register_survey_handlers(bot)