---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-100
title: bt_le_cs_test_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__test__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_bt\_le\_cs\_test\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__test__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

信道探测测试（CS Test）的回调。

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="details"></a>

信道探测测试（CS Test）的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 100.1\_数据成员（Data Fields）

<a id="r_a2a3ca580a3c3d55aa2f2323a318827f9"></a>

```c
void(* le_cs_test_subevent_data_available )(struct bt_conn_le_cs_subevent_result *data)
```

相关声明：[le_cs_test_subevent_data_available](#a2a3ca580a3c3d55aa2f2323a318827f9)、[bt_conn_le_cs_subevent_result](P018_bt_conn_le_cs_subevent_result_结构体.md)。

信道探测测试子事件数据（CS Test Subevent data）。

<a id="r_a7da5731fb2ae9e7fc3cece78a7468663"></a>

```c
void(* le_cs_test_end_complete )(void)
```

相关声明：[le_cs_test_end_complete](#a7da5731fb2ae9e7fc3cece78a7468663)。

信道探测测试结束完成（CS Test End Complete）。

## 100.2\_详细说明（Detailed Documentation）

<a id="a7da5731fb2ae9e7fc3cece78a7468663"></a>

### `le_cs_test_end_complete`

```c
void(* bt_le_cs_test_cb::le_cs_test_end_complete) (void)
```

信道探测测试结束完成（CS Test End Complete）。

<a id="a2a3ca580a3c3d55aa2f2323a318827f9"></a>

### `le_cs_test_subevent_data_available`

```c
void(* bt_le_cs_test_cb::le_cs_test_subevent_data_available) (struct bt_conn_le_cs_subevent_result *data)
```

信道探测测试子事件数据（CS Test Subevent data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] data` | 子事件结果（Subevent results）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/cs.h`

## 100.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/cs.h](https://docs.zephyrproject.org/latest/doxygen/html/cs_8h_source.html)
- [bt_conn_le_cs_subevent_result](P018_bt_conn_le_cs_subevent_result_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P099_bt_le_cs_subevent_step_结构体.md) · [返回大纲](大纲.md) · [下一章](P101_bt_le_cs_test_param_结构体.md)
