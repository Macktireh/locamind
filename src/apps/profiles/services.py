from apps.common.services import model_update
from apps.profiles.models import Profile
from apps.profiles.types import ProfilePayloadType


class ProfileService:
    profile = Profile

    def create(self, payload: ProfilePayloadType) -> Profile:
        return self.profile.objects.create(**payload)

    def update_user_profile(self, profile: Profile, data: dict) -> Profile:
        """
        Update user data only for the fields 'phone_number'.
        """
        non_side_effect_fields = ["phone_number"]
        profile, has_updated = model_update(instance=profile, fields=non_side_effect_fields, data=data)
        return profile


profile_service = ProfileService()
