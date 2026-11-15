---
id: learning.zephyr-docs.networking.api-185
title: MCP服务器头文件源码
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcp__server_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第185章\_MCP服务器头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mcp__server_8h_source.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 185.1\_阅读说明与来源

译注：先读[模型上下文协议服务器指南](P178_MCP服务器.md)与[服务器入门示例](P181_MCP服务器入门示例.md)，理解服务器上下文（Server Context）、工具回调（Tool Callback）、执行令牌（Execution Token）和传输层（Transport）的关系，再按符号查询本组参考。

本组：[MCP完整API参考](P183_MCP完整API参考.md) · [MCP服务器头文件参考](P184_MCP服务器头文件参考.md) · [MCP服务器头文件源码](P185_MCP服务器头文件源码.md) · [MCP的HTTP头文件参考](P186_MCP的HTTP头文件参考.md) · [MCP的HTTP头文件源码](P187_MCP的HTTP头文件源码.md) · [MCP工具消息结构](P188_MCP工具消息结构.md) · [MCP工具元数据结构](P189_MCP工具元数据结构.md) · [MCP工具记录结构](P190_MCP工具记录结构.md)。

下方保留官方 Doxygen 源码浏览页展示的全部代码、标识符和版权／许可注释。仅移除网页行号，将展示用不换行空格还原为空格，并清除行尾空白。原页面已省略用于生成 API 文档的部分注释，行号原本存在跳跃；本展示不能替代完整原始头文件。接口、参数和结构体注释均在本组参考页翻译。

## 185.2\_原始源码展示

<a id="l00001"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__mcp__server_html_ga1668b35e8e2e32d1e5e4c1d68561c5fe"></a>
<a id="agroup__mcp__server_html_ga37df157c8a497affb24610d66096f6ae"></a>
<a id="agroup__mcp__server_html_ga3e08a0cb026f941ca9d68a2636c3f33e"></a>
<a id="agroup__mcp__server_html_ga4ea4339861b61e14403856a18a8ef065"></a>
<a id="agroup__mcp__server_html_ga5614c519ddad03f9cc51c7354b7029f1"></a>
<a id="agroup__mcp__server_html_ga738c6574f367615b8818534a4827258d"></a>
<a id="agroup__mcp__server_html_ga90a431894013659b5a9ca7e49ed38f34"></a>
<a id="agroup__mcp__server_html_ga9897522e100bc6d84aaaf450871fc30a"></a>
<a id="agroup__mcp__server_html_gacb8dc5cf60b9f4bad1486f89330e62ad"></a>
<a id="agroup__mcp__server_html_gadef2d994c7bebd418531b597040a1f7d"></a>
<a id="agroup__mcp__server_html_gga4ea4339861b61e14403856a18a8ef065a6694d4b9c7f1fe70f5c9e410affbf5d1"></a>
<a id="agroup__mcp__server_html_gga4ea4339861b61e14403856a18a8ef065a9ae0010b1615a9febaa953b00b5d3d1e"></a>
<a id="agroup__mcp__server_html_gga9897522e100bc6d84aaaf450871fc30aa5a339272d44f32c7b46039d25e45d814"></a>
<a id="agroup__mcp__server_html_gga9897522e100bc6d84aaaf450871fc30aa8b38fbd2577eca5a8c9c0e76b39c5ea1"></a>
<a id="agroup__mcp__server_html_gga9897522e100bc6d84aaaf450871fc30aaa7435cada70d1ebe4e6f4fef611b152d"></a>
<a id="agroup__mcp__server_html_gga9897522e100bc6d84aaaf450871fc30aaafcad745a3538eba10b081a457941499"></a>
<a id="akernel_8h_html"></a>
<a id="astructmcp__tool__message_html"></a>
<a id="astructmcp__tool__message_html_a19e7156f6e167469df002e7725ea4b38"></a>
<a id="astructmcp__tool__message_html_a2dc79941b1942586dd0e266765d6c311"></a>
<a id="astructmcp__tool__message_html_a5d874717b19d6fd604965d3a3ed7be9e"></a>
<a id="astructmcp__tool__message_html_a78cd6d69444ed412a52ee9bb37b30352"></a>
<a id="astructmcp__tool__metadata_html"></a>
<a id="astructmcp__tool__metadata_html_a6499a3e806f41d568c711c3f0b617515"></a>
<a id="astructmcp__tool__metadata_html_acbccf4378024dd406563035b85bfc5d4"></a>
<a id="astructmcp__tool__record_html"></a>
<a id="astructmcp__tool__record_html_a170d9355504262208defe6e4cb75f509"></a>
<a id="astructmcp__tool__record_html_a24e2b950dedb31b39ff503d1c8966b78"></a>
<a id="astructmcp__tool__record_html_a73b011610654fc8bf1fffd07c0ff9dde"></a>

```c


/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_MCP_MCP_SERVER_H_
#define ZEPHYR_INCLUDE_NET_MCP_MCP_SERVER_H_


#include <zephyr/kernel.h>
#include <errno.h>

#ifdef __cplusplus
extern "C" {
#endif

enum mcp_tool_msg_type {
        MCP_USR_TOOL_RESPONSE,
        MCP_USR_TOOL_NOTIFICATION,
        MCP_USR_TOOL_CANCEL_ACK,
        MCP_USR_TOOL_PING
};

enum mcp_tool_event_type {
        MCP_TOOL_CALL_REQUEST,
        MCP_TOOL_CANCEL_REQUEST
};

struct mcp_tool_metadata {
        char name[CONFIG_MCP_TOOL_NAME_MAX_LEN];
        char input_schema[CONFIG_MCP_TOOL_SCHEMA_MAX_LEN];
#ifdef CONFIG_MCP_TOOL_DESC
        char description[CONFIG_MCP_TOOL_DESC_MAX_LEN];
#endif
#ifdef CONFIG_MCP_TOOL_TITLE
        char title[CONFIG_MCP_TOOL_NAME_MAX_LEN];
#endif
#ifdef CONFIG_MCP_TOOL_OUTPUT_SCHEMA
        char output_schema[CONFIG_MCP_TOOL_SCHEMA_MAX_LEN];
#endif
};

typedef void *mcp_server_ctx_t;

typedef int (*mcp_tool_callback_t)(enum mcp_tool_event_type event, const char *arguments,
                                   const char *execution_token);

struct mcp_tool_record {
        struct mcp_tool_metadata metadata;
        atomic_t refcount;
        mcp_tool_callback_t callback;
};

struct mcp_tool_message {
        enum mcp_tool_msg_type type;
        int length;
        void *data;
        bool is_error;
};

mcp_server_ctx_t mcp_server_init(void);

int mcp_server_start(mcp_server_ctx_t server_ctx);

int mcp_server_submit_tool_message(mcp_server_ctx_t server_ctx,
                                   const struct mcp_tool_message *user_msg,
                                   const char *execution_token);

int mcp_server_add_tool(mcp_server_ctx_t server_ctx, const struct mcp_tool_record *tool_record);

int mcp_server_remove_tool(mcp_server_ctx_t server_ctx, const char *tool_name);

int mcp_server_is_execution_canceled(mcp_server_ctx_t server_ctx, const char *execution_token,
                                     bool *is_canceled);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_MCP_MCP_SERVER_H_ */
```

## 185.3\_源码注释译文

版权：2025 年 NXP；许可证标识为 `Apache-2.0`。原始法律署名保持原样。末尾 `#endif` 注释表示结束头文件包含保护（Header Include Guard）。核心头文件的 `extern "C"` 条件块为 C++ 调用方提供 C 链接约定。

## 185.4\_相关源码与使用边界

声明来自 `<zephyr/net/mcp/mcp_server.h>` 及 `<zephyr/net/mcp/mcp_server_http.h>`。本仓库的[核心头文件](../../../include/zephyr/net/mcp/mcp_server.h)和[HTTP 头文件](../../../include/zephyr/net/mcp/mcp_server_http.h)可用于源码追踪，版本可能与官网 `latest` 不同。以下核对依据为本批保存的[官方核心实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server.c)及[官方 HTTP 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server_http.c)，源码摘要见[来源记录](../SOURCES.md)。

[上一章](P184_MCP服务器头文件参考.md) · [返回大纲](大纲.md) · [下一章](P186_MCP的HTTP头文件参考.md)
