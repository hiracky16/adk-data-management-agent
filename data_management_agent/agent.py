import os
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

TOOLBOX_URL = os.getenv("TOOLBOX_URL", "http://localhost:5001")
toolbox = ToolboxSyncClient(TOOLBOX_URL)

tools = toolbox.load_toolset("company-master-management")

INSTRUCTION = """
  あなたは企業データを管理するAIアシスタントです。以下のツールを使って、企業データの検索、追加、削除を行うことができます。

  企業データはcompany_masterテーブルに保存されており、以下のカラムがあります:
  - id (INT): 企業の一意の識別子
  - name (STRING): 企業名
  - corporate_number (STRING): 法人番号
  - location (STRING): 企業の所在地
  - deleted_at (DATE): 企業が削除された日時（削除されていない場合はNULL）
  あなたのタスクは、ユーザーからのリクエストに基づいて、適切なツールを選択し、企業データを管理することです。

  ツール一覧
  - list-companies: すべての企業データを取得します。
  - search-companies-by-name: 企業名で企業データを検索します。
  - add-company: 新しい企業データを追加します。
  - delete-company: 企業データを削除します。
  - init-company-master: company_masterテーブルを初期化します（テスト用）。
  - update-corporate-number: 企業の法人番号を更新します。
  - update-company-name: 企業名を更新します。

  注意点:
  - ユーザーからのリクエストに対して、最も適切なツールを選択し、必要なパラメータを提供してください。
  - 企業データの削除は論理削除で行い、deleted_atカラムに削除日時を設定してください。
  - 法人番号は 13 桁の数字で構成されていることを確認してください。
"""

google_search_tool = AgentTool(
    agent=Agent(
        model="gemini-2.5-flash",
        name="google_search_agent",
        description="A helpful AI assistant that can search company information.",
        instruction="あなたは企業情報のリサーチャーです。Google検索を用いて企業情報を調査してください。",
        tools=[google_search],
    )
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="data_management_agent",
    description="A helpful AI assistant that can manage data.",
    instruction=INSTRUCTION,
    tools=tools + [google_search_tool],
)
