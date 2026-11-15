---
id: learning.zephyr-docs.modem-wireless-model-reference.page-18
title: hl78xx_at_notification_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__at__notification.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_hl78xx\_at\_notification\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__at__notification.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已解析的主动AT通知（Unsolicited AT Notification）载荷。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

已解析的非请求 AT 通知载荷。`pattern` 字段是 HL78xx 驱动表中的规范化非请求匹配模式，`argv[0]` 则包含 `modem_chat` 生成的实际匹配词元（token）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_ac5e4004e705d5675716603171582a01c"></a>

```c
const char * pattern
```

相关声明：[pattern](#ac5e4004e705d5675716603171582a01c)。

来自驱动表的规范化非请求匹配模式。

<a id="r_a36fd5f326795ace901b6ab0dc22ef934"></a>

```c
const char *const * argv
```

相关声明：[argv](#a36fd5f326795ace901b6ab0dc22ef934)。

已解析参数，其中 `argv[0]` 是实际匹配的词元。

<a id="r_ad2cd1746e6a6eb2cca28d831de31d798"></a>

```c
uint16_t argc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[argc](#ad2cd1746e6a6eb2cca28d831de31d798)。

已解析参数数量。

## 18.2\_详细说明（Detailed Documentation）

<a id="ad2cd1746e6a6eb2cca28d831de31d798"></a>

### `argc`

```c
uint16_t hl78xx_at_notification::argc
```

已解析参数数量。

<a id="a36fd5f326795ace901b6ab0dc22ef934"></a>

### `argv`

```c
const char* const* hl78xx_at_notification::argv
```

已解析参数，其中 `argv[0]` 是实际匹配的词元。

<a id="ac5e4004e705d5675716603171582a01c"></a>

### `pattern`

```c
const char* hl78xx_at_notification::pattern
```

来自驱动表的规范化非请求匹配模式。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_chat](P052_modem_chat_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_hl78xx_at_monitor_entry_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_hl78xx_ctzeu_update_结构体.md)
