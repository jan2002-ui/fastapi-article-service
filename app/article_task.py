# app/state/article_task.py
import asyncio

article_task: asyncio.Task | None = None
stop_event = asyncio.Event()
