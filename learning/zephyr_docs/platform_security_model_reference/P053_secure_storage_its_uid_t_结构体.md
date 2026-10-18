---
id: learning.zephyr-docs.platform-security-model-reference.page-53
title: secure_storage_its_uid_t_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsecure__storage__its__uid__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_secure\_storage\_its\_uid\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsecure__storage__its__uid__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内部可信存储（ITS）条目的UID，由调用方ID与条目ID组成。

```c
#include <zephyr/secure_storage/its/common.h>
```

<a id="details"></a>

内部可信存储（Internal Trusted Storage，ITS）条目的 UID，由调用方 ID 和条目 ID 组成。这是 `psa_storage_uid_t` 的紧凑 32 位版本，相比 PSA 安全存储（PSA Secure Storage）规定的 64 位 ID，可以存储较小的 ID。Zephyr 为 API 的不同使用方（子系统、应用程序）定义各自的 ID 范围，保证：1. ID 不冲突；2. 所使用的 ID 均能装入 `uid`。另请参阅 `zephyr/psa/key_ids.h` 以及 `zephyr/psa` 下的其他头文件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_a444f3c47521ef82e086c0c43941e23ee"></a>

```c
psa_storage_uid_t uid: 30
```

相关声明：[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)、[uid](#a444f3c47521ef82e086c0c43941e23ee)。

<a id="r_a8f581033ce88a130f3a6b04c9821294e"></a>

```c
secure_storage_its_caller_id_t caller_id: 2
```

相关声明：[secure_storage_its_caller_id_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a2369ff303bf323cb4e57f1b970093d2b)、[caller_id](#a8f581033ce88a130f3a6b04c9821294e)。

## 53.2\_详细说明（Detailed Documentation）

<a id="a8f581033ce88a130f3a6b04c9821294e"></a>

### `caller_id`

```c
secure_storage_its_caller_id_t secure_storage_its_uid_t::caller_id
```

<a id="a444f3c47521ef82e086c0c43941e23ee"></a>

### `uid`

```c
psa_storage_uid_t secure_storage_its_uid_t::uid
```

本数据类型文档由以下文件生成：

- `/__w/zephyr/zephyr/subsys/secure_storage/include/internal/zephyr/secure_storage/its/common.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/secure_storage/its/common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.html)
- [psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)
- [secure_storage_its_caller_id_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a2369ff303bf323cb4e57f1b970093d2b)
- [zephyr/psa/key_ids.h](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_scmi_transport_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_shared_irq_driver_api_结构体.md)
