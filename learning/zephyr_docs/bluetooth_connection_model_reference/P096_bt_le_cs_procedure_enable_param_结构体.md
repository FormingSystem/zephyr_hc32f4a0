---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-96
title: bt_le_cs_procedure_enable_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__procedure__enable__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_bt\_le\_cs\_procedure\_enable\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__procedure__enable__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 96.1\_数据成员（Data Fields）

<a id="r_aa776933876805f8e7074abbf47634ea4"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#aa776933876805f8e7074abbf47634ea4)。

<a id="r_a01416dc5ed8f0315f050f76ce8ca3034"></a>

```c
enum bt_conn_le_cs_procedure_enable_state enable
```

相关声明：[bt_conn_le_cs_procedure_enable_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3653de72793f775e33fd9eb04c3e7a2)、[enable](#a01416dc5ed8f0315f050f76ce8ca3034)。

## 96.2\_详细说明（Detailed Documentation）

<a id="aa776933876805f8e7074abbf47634ea4"></a>

### `config_id`

```c
uint8_t bt_le_cs_procedure_enable_param::config_id
```

<a id="a01416dc5ed8f0315f050f76ce8ca3034"></a>

### `enable`

```c
enum bt_conn_le_cs_procedure_enable_state bt_le_cs_procedure_enable_param::enable
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/cs.h`

## 96.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/cs.h](https://docs.zephyrproject.org/latest/doxygen/html/cs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn_le_cs_procedure_enable_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3653de72793f775e33fd9eb04c3e7a2)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P095_bt_le_cs_iq_sample_结构体.md) · [返回大纲](大纲.md) · [下一章](P097_bt_le_cs_set_default_settings_param_结构体.md)
