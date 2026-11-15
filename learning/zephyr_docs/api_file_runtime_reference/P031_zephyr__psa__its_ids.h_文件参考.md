---
id: learning.zephyr-docs.api-file-runtime-reference.page-31
title: zephyr__psa__its_ids.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/its__ids_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_psa\_\_its\_ids.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/its__ids_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

此文件定义PSA内部可信存储（ITS）API现有使用者的UID范围。

查看此文件的源码。

<a id="details"></a>

本文件定义 PSA 内部可信存储 API（PSA ITS API）现有使用者的唯一标识范围（UID Ranges）。另请参见（See Also）`zephyr/psa/key_ids.h`。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 31.1\_宏定义（Macros）

<a id="r_a85d68fa5575b315f82ac9c910f4458fc"></a>

```c
#define ZEPHYR_PSA_SETTINGS_TFM_ITS_UID_RANGE_BEGIN 0x28000000
```

相关声明：[ZEPHYR_PSA_SETTINGS_TFM_ITS_UID_RANGE_BEGIN](#a85d68fa5575b315f82ac9c910f4458fc)。

供 TF-M PSA ITS 设置后端（Settings Backend）使用的唯一标识范围（UID Range）。

<a id="r_a323b299b2275404bd76fc0341876d47a"></a>

```c
#define ZEPHYR_PSA_SETTINGS_TFM_ITS_UID_RANGE_SIZE 0x10000
```

相关声明：[ZEPHYR_PSA_SETTINGS_TFM_ITS_UID_RANGE_SIZE](#a323b299b2275404bd76fc0341876d47a)。

64 Ki（64 × 1024）。

## 31.2\_详细说明（Detailed Documentation）

<a id="a85d68fa5575b315f82ac9c910f4458fc"></a>

### `ZEPHYR_PSA_SETTINGS_TFM_ITS_UID_RANGE_BEGIN`

```c
#define ZEPHYR_PSA_SETTINGS_TFM_ITS_UID_RANGE_BEGIN 0x28000000
```

供 TF-M PSA ITS 设置后端（Settings Backend）使用的唯一标识范围（UID Range）。

<a id="a323b299b2275404bd76fc0341876d47a"></a>

### `ZEPHYR_PSA_SETTINGS_TFM_ITS_UID_RANGE_SIZE`

```c
#define ZEPHYR_PSA_SETTINGS_TFM_ITS_UID_RANGE_SIZE 0x10000
```

64 Ki（64 × 1024）。


## 31.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P425_its_ids.h_源码浏览.md)
- [zephyr/psa/key_ids.h](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P030_zephyr__dt-bindings__sensor__it8xxx2_tach.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__bluetooth__mesh__large_comp_data_cli.h_文件参考.md)
