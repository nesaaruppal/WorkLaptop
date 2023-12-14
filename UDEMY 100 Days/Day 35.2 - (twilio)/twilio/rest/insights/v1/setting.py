r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, Optional, Union
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SettingInstance(InstanceResource):

    """
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar advanced_features: A boolean flag indicating whether Advanced Features for Voice Insights are enabled.
    :ivar voice_trace: A boolean flag indicating whether Voice Trace is enabled.
    :ivar url: The URL of this resource.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.advanced_features: Optional[bool] = payload.get("advanced_features")
        self.voice_trace: Optional[bool] = payload.get("voice_trace")
        self.url: Optional[str] = payload.get("url")

        self._context: Optional[SettingContext] = None

    @property
    def _proxy(self) -> "SettingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SettingContext for this SettingInstance
        """
        if self._context is None:
            self._context = SettingContext(
                self._version,
            )
        return self._context

    def fetch(
        self, subaccount_sid: Union[str, object] = values.unset
    ) -> "SettingInstance":
        """
        Fetch the SettingInstance

        :param subaccount_sid: The unique SID identifier of the Subaccount.

        :returns: The fetched SettingInstance
        """
        return self._proxy.fetch(
            subaccount_sid=subaccount_sid,
        )

    async def fetch_async(
        self, subaccount_sid: Union[str, object] = values.unset
    ) -> "SettingInstance":
        """
        Asynchronous coroutine to fetch the SettingInstance

        :param subaccount_sid: The unique SID identifier of the Subaccount.

        :returns: The fetched SettingInstance
        """
        return await self._proxy.fetch_async(
            subaccount_sid=subaccount_sid,
        )

    def update(
        self,
        advanced_features: Union[bool, object] = values.unset,
        voice_trace: Union[bool, object] = values.unset,
        subaccount_sid: Union[str, object] = values.unset,
    ) -> "SettingInstance":
        """
        Update the SettingInstance

        :param advanced_features: A boolean flag to enable Advanced Features for Voice Insights.
        :param voice_trace: A boolean flag to enable Voice Trace.
        :param subaccount_sid: The unique SID identifier of the Subaccount.

        :returns: The updated SettingInstance
        """
        return self._proxy.update(
            advanced_features=advanced_features,
            voice_trace=voice_trace,
            subaccount_sid=subaccount_sid,
        )

    async def update_async(
        self,
        advanced_features: Union[bool, object] = values.unset,
        voice_trace: Union[bool, object] = values.unset,
        subaccount_sid: Union[str, object] = values.unset,
    ) -> "SettingInstance":
        """
        Asynchronous coroutine to update the SettingInstance

        :param advanced_features: A boolean flag to enable Advanced Features for Voice Insights.
        :param voice_trace: A boolean flag to enable Voice Trace.
        :param subaccount_sid: The unique SID identifier of the Subaccount.

        :returns: The updated SettingInstance
        """
        return await self._proxy.update_async(
            advanced_features=advanced_features,
            voice_trace=voice_trace,
            subaccount_sid=subaccount_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Insights.V1.SettingInstance>"


class SettingContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the SettingContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/Voice/Settings"

    def fetch(
        self, subaccount_sid: Union[str, object] = values.unset
    ) -> SettingInstance:
        """
        Fetch the SettingInstance

        :param subaccount_sid: The unique SID identifier of the Subaccount.

        :returns: The fetched SettingInstance
        """

        data = values.of(
            {
                "SubaccountSid": subaccount_sid,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return SettingInstance(
            self._version,
            payload,
        )

    async def fetch_async(
        self, subaccount_sid: Union[str, object] = values.unset
    ) -> SettingInstance:
        """
        Asynchronous coroutine to fetch the SettingInstance

        :param subaccount_sid: The unique SID identifier of the Subaccount.

        :returns: The fetched SettingInstance
        """

        data = values.of(
            {
                "SubaccountSid": subaccount_sid,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return SettingInstance(
            self._version,
            payload,
        )

    def update(
        self,
        advanced_features: Union[bool, object] = values.unset,
        voice_trace: Union[bool, object] = values.unset,
        subaccount_sid: Union[str, object] = values.unset,
    ) -> SettingInstance:
        """
        Update the SettingInstance

        :param advanced_features: A boolean flag to enable Advanced Features for Voice Insights.
        :param voice_trace: A boolean flag to enable Voice Trace.
        :param subaccount_sid: The unique SID identifier of the Subaccount.

        :returns: The updated SettingInstance
        """
        data = values.of(
            {
                "AdvancedFeatures": advanced_features,
                "VoiceTrace": voice_trace,
                "SubaccountSid": subaccount_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SettingInstance(self._version, payload)

    async def update_async(
        self,
        advanced_features: Union[bool, object] = values.unset,
        voice_trace: Union[bool, object] = values.unset,
        subaccount_sid: Union[str, object] = values.unset,
    ) -> SettingInstance:
        """
        Asynchronous coroutine to update the SettingInstance

        :param advanced_features: A boolean flag to enable Advanced Features for Voice Insights.
        :param voice_trace: A boolean flag to enable Voice Trace.
        :param subaccount_sid: The unique SID identifier of the Subaccount.

        :returns: The updated SettingInstance
        """
        data = values.of(
            {
                "AdvancedFeatures": advanced_features,
                "VoiceTrace": voice_trace,
                "SubaccountSid": subaccount_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SettingInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Insights.V1.SettingContext>"


class SettingList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SettingList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> SettingContext:
        """
        Constructs a SettingContext

        """
        return SettingContext(self._version)

    def __call__(self) -> SettingContext:
        """
        Constructs a SettingContext

        """
        return SettingContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.SettingList>"
