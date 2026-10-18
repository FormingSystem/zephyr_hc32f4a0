---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-148
title: bt_pacs_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__pacs__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第148章\_bt\_pacs\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__pacs__register__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于注册已发布音频能力服务（PACS）的结构。

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

<a id="details"></a>

用于注册已发布音频能力服务（PACS）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 148.1\_数据成员（Data Fields）

<a id="r_a7b5d14b7206a593821af96343120edbb"></a>

```c
bool snk_pac
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[snk_pac](#a7b5d14b7206a593821af96343120edbb)。

启用或禁用接收端已发布音频能力（Sink PAC）特征的注册。

<a id="r_a3eda569266531da60342f0a170c4d152"></a>

```c
bool snk_loc
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[snk_loc](#a3eda569266531da60342f0a170c4d152)。

启用或禁用接收端位置（Sink Location）特征的注册。

<a id="r_a922188bb4e989aabb6b4cbba43d457c8"></a>

```c
bool src_pac
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[src_pac](#a922188bb4e989aabb6b4cbba43d457c8)。

启用或禁用发送端已发布音频能力（Source PAC）特征的注册。

<a id="r_af377b54efe30f22f4bfb1677964a1f00"></a>

```c
bool src_loc
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[src_loc](#af377b54efe30f22f4bfb1677964a1f00)。

启用或禁用发送端位置（Source Location）特征的注册。

## 148.2\_详细说明（Detailed Documentation）

<a id="a3eda569266531da60342f0a170c4d152"></a>

### `snk_loc`

```c
bool bt_pacs_register_param::snk_loc
```

启用或禁用接收端位置（Sink Location）特征的注册。

注册接收端位置（Sink Location）的前提是同时设置 `bt_pacs_register_param::snk_pac`。

<a id="a7b5d14b7206a593821af96343120edbb"></a>

### `snk_pac`

```c
bool bt_pacs_register_param::snk_pac
```

启用或禁用接收端已发布音频能力（Sink PAC）特征的注册。

<a id="af377b54efe30f22f4bfb1677964a1f00"></a>

### `src_loc`

```c
bool bt_pacs_register_param::src_loc
```

启用或禁用发送端位置（Source Location）特征的注册。

注册发送端位置（Source Location）的前提是同时设置 `bt_pacs_register_param::src_pac`。

<a id="a922188bb4e989aabb6b4cbba43d457c8"></a>

### `src_pac`

```c
bool bt_pacs_register_param::src_pac
```

启用或禁用发送端已发布音频能力（Source PAC）特征的注册。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/pacs.h`

## 148.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/pacs.h](https://docs.zephyrproject.org/latest/doxygen/html/pacs_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P147_bt_pacs_cap_结构体.md) · [返回大纲](大纲.md) · [下一章](P149_bt_pbap_pce_结构体.md)
