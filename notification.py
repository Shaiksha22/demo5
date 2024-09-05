from pynotifier import Notification
Notification(
    tittle="solo",
    description="welcome solo , you have 5 unread messeges",
    duration=30,
    urgency=Notification.URGENCY_CRITICAL).send()
