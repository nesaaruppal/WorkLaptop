r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class TaskQueueStatisticsInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskQueue resource.
    :ivar cumulative: An object that contains the cumulative statistics for the TaskQueue.
    :ivar realtime: An object that contains the real-time statistics for the TaskQueue.
    :ivar task_queue_sid: The SID of the TaskQueue from which these statistics were calculated.
    :ivar workspace_sid: The SID of the Workspace that contains the TaskQueue.
    :ivar url: The absolute URL of the TaskQueue statistics resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        workspace_sid: str,
        task_queue_sid: str,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.cumulative: Optional[Dict[str, object]] = payload.get("cumulative")
        self.realtime: Optional[Dict[str, object]] = payload.get("realtime")
        self.task_queue_sid: Optional[str] = payload.get("task_queue_sid")
        self.workspace_sid: Optional[str] = payload.get("workspace_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "workspace_sid": workspace_sid,
            "task_queue_sid": task_queue_sid,
        }
        self._context: Optional[TaskQueueStatisticsContext] = None

    @property
    def _proxy(self) -> "TaskQueueStatisticsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskQueueStatisticsContext for this TaskQueueStatisticsInstance
        """
        if self._context is None:
            self._context = TaskQueueStatisticsContext(
                self._version,
                workspace_sid=self._solution["workspace_sid"],
                task_queue_sid=self._solution["task_queue_sid"],
            )
        return self._context

    def fetch(
        self,
        end_date: Union[datetime, object] = values.unset,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> "TaskQueueStatisticsInstance":
        """
        Fetch the TaskQueueStatisticsInstance

        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param task_channel: Only calculate real-time and cumulative statistics for the specified TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.

        :returns: The fetched TaskQueueStatisticsInstance
        """
        return self._proxy.fetch(
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
        )

    async def fetch_async(
        self,
        end_date: Union[datetime, object] = values.unset,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> "TaskQueueStatisticsInstance":
        """
        Asynchronous coroutine to fetch the TaskQueueStatisticsInstance

        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param task_channel: Only calculate real-time and cumulative statistics for the specified TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.

        :returns: The fetched TaskQueueStatisticsInstance
        """
        return await self._proxy.fetch_async(
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.TaskQueueStatisticsInstance {}>".format(context)


class TaskQueueStatisticsContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str, task_queue_sid: str):
        """
        Initialize the TaskQueueStatisticsContext

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
        :param task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "task_queue_sid": task_queue_sid,
        }
        self._uri = (
            "/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/Statistics".format(
                **self._solution
            )
        )

    def fetch(
        self,
        end_date: Union[datetime, object] = values.unset,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> TaskQueueStatisticsInstance:
        """
        Fetch the TaskQueueStatisticsInstance

        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param task_channel: Only calculate real-time and cumulative statistics for the specified TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.

        :returns: The fetched TaskQueueStatisticsInstance
        """

        data = values.of(
            {
                "EndDate": serialize.iso8601_datetime(end_date),
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "TaskChannel": task_channel,
                "SplitByWaitTime": split_by_wait_time,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return TaskQueueStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            task_queue_sid=self._solution["task_queue_sid"],
        )

    async def fetch_async(
        self,
        end_date: Union[datetime, object] = values.unset,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> TaskQueueStatisticsInstance:
        """
        Asynchronous coroutine to fetch the TaskQueueStatisticsInstance

        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param task_channel: Only calculate real-time and cumulative statistics for the specified TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.

        :returns: The fetched TaskQueueStatisticsInstance
        """

        data = values.of(
            {
                "EndDate": serialize.iso8601_datetime(end_date),
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "TaskChannel": task_channel,
                "SplitByWaitTime": split_by_wait_time,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return TaskQueueStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            task_queue_sid=self._solution["task_queue_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.TaskQueueStatisticsContext {}>".format(context)


class TaskQueueStatisticsList(ListResource):
    def __init__(self, version: Version, workspace_sid: str, task_queue_sid: str):
        """
        Initialize the TaskQueueStatisticsList

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
        :param task_queue_sid: The SID of the TaskQueue for which to fetch statistics.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "task_queue_sid": task_queue_sid,
        }

    def get(self) -> TaskQueueStatisticsContext:
        """
        Constructs a TaskQueueStatisticsContext

        """
        return TaskQueueStatisticsContext(
            self._version,
            workspace_sid=self._solution["workspace_sid"],
            task_queue_sid=self._solution["task_queue_sid"],
        )

    def __call__(self) -> TaskQueueStatisticsContext:
        """
        Constructs a TaskQueueStatisticsContext

        """
        return TaskQueueStatisticsContext(
            self._version,
            workspace_sid=self._solution["workspace_sid"],
            task_queue_sid=self._solution["task_queue_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Taskrouter.V1.TaskQueueStatisticsList>"
