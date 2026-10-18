---
id: learning.zephyr-docs.developer-tools.kapa
title: Kapa.ai文档助手
kind: reference
status: maintained
domains: [zephyr, tools, development]
source_url: https://docs.zephyrproject.org/latest/develop/tools/kapa_ai.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_Kapa.ai文档助手

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/tools/kapa_ai.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

<a id="kapa-ai"></a>

<a id="kapa-ai-documentation-assistant"></a>

Zephyr文档网站集成了由Kapa.ai提供的人工智能（Artificial Intelligence，AI）助手。该助手以Zephyr自身的文档、源码和GitHub活动为训练依据，详见[数据来源](#data-sources)。它可以用自然语言回答自由形式的问题，并引用生成答案时使用的文档页面和资源。

同一知识库还通过[模型上下文协议（Model Context Protocol，MCP）](https://modelcontextprotocol.io/)服务器提供，使外部AI助手和IDE可以直接查询Zephyr知识，详见[使用MCP服务器](#using-the-mcp-server)。

> 注意（Note）：答案由AI生成，可能存在错误。重要信息应始终对照官方文档核实，应将助手作为查询起点，而非权威来源。

<a id="using-the-chatbot"></a>

## 8.1\_使用聊天助手

每个文档页面都可以使用聊天助手：点击页面底部的聊天助手按钮，或在任意位置按`Ctrl+K`（macOS上为`Cmd+K`）打开。

助手在侧栏中打开，可以用日常语言提问，例如“如何在设备树中配置UART设备？”或“工作队列和线程有什么区别？”。答案会附上相关文档页面、GitHub议题（Issue）或源文件链接，便于进一步了解。

首次使用时会出现一次性的同意界面，解释功能的工作方式及收集的数据，详见[隐私](#privacy)。

> 提示（Tip）：不必使用英语提问。助手会检测提问语言并使用相同语言回答，可以使用英语、中文、西班牙语、日语、法语、德语等多种语言。

<a id="ai-powered-search"></a>

## 8.2\_AI搜索

除了聊天助手，Kapa.ai还可以为文档搜索框提供支持：

1. 点击搜索框旁的齿轮图标，即 **Search settings**（搜索设置）。
2. 从菜单选择 **Kapa AI search**。
3. 输入查询并按`Enter`。

此时由AI助手回答查询，替代内置关键词搜索。所选引擎会被记住，后续搜索将继续使用它，直到再次更改。

<a id="using-the-mcp-server"></a>

## 8.3\_使用MCP服务器

Kapa.ai还将Zephyr知识库公开为MCP服务器。MCP是开放标准，使AI助手和支持AI的IDE能够连接外部工具与知识来源。将Zephyr MCP服务器添加到助手后，助手便能够代表用户查询最新的Zephyr文档、源码和GitHub活动。

服务器通过以下端点提供服务，使用可流式HTTP传输（Streamable HTTP Transport）：

```text
https://zephyrproject.mcp.kapa.ai
```

具体配置步骤取决于所使用的MCP客户端。多数客户端读取JSON配置文件，其中包含类似下面的`mcpServers`部分：

```json
{
  "mcpServers": {
    "zephyr-docs": {
      "url": "https://zephyrproject.mcp.kapa.ai"
    }
  }
}
```

某些客户端则要求通过本地标准输入／输出（stdio）桥接程序启动服务器，例如[`mcp-remote`](https://www.npmjs.com/package/mcp-remote)：

```json
{
  "mcpServers": {
    "zephyr-docs": {
      "command": "npx", "args": ["-y", "mcp-remote", "https://zephyrproject.mcp.kapa.ai"]
    }
  }
}
```

配置文件的准确位置和语法，应参考所用MCP客户端的文档，例如AI编程助手或IDE扩展的文档。

> 提示（Tip）：将MCP服务器连接到AI编程助手后，助手可以回答Zephyr问题，并以项目实际文档和源码作为代码建议的依据，而不只是依赖训练数据。

<a id="data-sources"></a>

## 8.4\_数据来源

Kapa.ai仅依据下列Zephyr项目来源生成答案，并按所列频率同步：

| 来源（Source） | 详情（Details） | 刷新频率（Refresh frequency） |
| --- | --- | --- |
| 源码（Source code） | `zephyrproject-rtos/zephyr`仓库，不包括`boards/`和`doc/`文件夹；包含C、Markdown、Python及文本文件。 | 每小时 |
| API参考（API reference） | [官方API参考](https://docs.zephyrproject.org/latest/doxygen/html/index.html) | 每天 |
| 设备树绑定（Devicetree bindings） | [官方设备树绑定](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html) | 每天 |
| 主文档（Main documentation） | [Zephyr官方文档](https://docs.zephyrproject.org/latest/)，不包括API参考与设备树绑定部分。 | 每天 |
| 项目Wiki（Project wiki） | [Zephyr项目Wiki](https://github.com/zephyrproject-rtos/zephyr/wiki) | 每天 |
| GitHub议题（GitHub issues） | `zephyrproject-rtos/zephyr`最近6个月的议题。 | 每5分钟 |
| GitHub拉取请求（GitHub pull requests） | `zephyrproject-rtos/zephyr`最近6个月的拉取请求，不包括未合并就关闭的请求。 | 每10分钟 |

权威且最新的配置请参见Zephyr项目基础设施Wiki中的[Kapa.ai页面](https://github.com/zephyrproject-rtos/infrastructure/wiki/Kapa.ai)。

<a id="privacy"></a>

## 8.5\_隐私

助手使用用户的问题，基于Zephyr文档、源码以及GitHub议题和拉取请求提供答案。问题和交互可能会以匿名方式收集和分析，用于发现需要澄清的内容，从而改进文档。原文说明不会收集可识别个人身份的信息（Personally Identifiable Information）。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Coccinelle](P007_Coccinelle.md) · [本模块主线目录](../reading/developer_tools.md) · [全部主线](../reading/README.md) · [下一篇：Zephyr开发指南入口](P009_开发指南入口.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Coccinelle](P007_Coccinelle.md) · [返回大纲](大纲.md) · [下一章：Zephyr开发指南入口](P009_开发指南入口.md)

</details>

<!-- reading-navigation:end -->
