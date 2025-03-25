import unittest
import asyncio
from unittest.mock import MagicMock, patch
from bot import make_issue  

class TestDiscordBot(unittest.TestCase):

    @patch('bot.jira.create_issue') 
    async def test_make_issue(self, mock_create_issue):
        ctx = MagicMock()
        ctx.message.reference = MagicMock(message_id=12345)
        ctx.channel.fetch_message = MagicMock(return_value=MagicMock(content="Test issue title"))

        mock_create_issue.return_value = MagicMock(key="TEST-1")

        await make_issue(ctx)

        ctx.send.assert_called_with("✅ Jira issue created: TEST-1")

def run_async_tests():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(unittest.main())

if __name__ == '__main__':
    run_async_tests()