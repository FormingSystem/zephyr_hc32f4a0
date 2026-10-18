---
id: learning.zephyr-docs.platform-security-model-reference.page-54
title: shared_irq_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshared__irq__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_shared\_irq\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshared__irq__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/shared_irq.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_a8e908b0d6e596905f11a3de1a6f907ad"></a>

```c
shared_irq_register_t isr_register
```

相关声明：[shared_irq_register_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#ae400920b45bedf3da66831597ebca841)、[isr_register](#a8e908b0d6e596905f11a3de1a6f907ad)。

<a id="r_a5a4ef3888a3d35497c47b67f4511fd5e"></a>

```c
shared_irq_enable_t enable
```

相关声明：[shared_irq_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#a0ff7a6ee448eb3e889aa9a7bd63e49bc)、[enable](#a5a4ef3888a3d35497c47b67f4511fd5e)。

<a id="r_a2e339779ddec773a536f681b9df9997e"></a>

```c
shared_irq_disable_t disable
```

相关声明：[shared_irq_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#a22cf2ce082fea27f2087cd1abd74934c)、[disable](#a2e339779ddec773a536f681b9df9997e)。

## 54.2\_详细说明（Detailed Documentation）

<a id="a2e339779ddec773a536f681b9df9997e"></a>

### `disable`

```c
shared_irq_disable_t shared_irq_driver_api::disable
```

<a id="a5a4ef3888a3d35497c47b67f4511fd5e"></a>

### `enable`

```c
shared_irq_enable_t shared_irq_driver_api::enable
```

<a id="a8e908b0d6e596905f11a3de1a6f907ad"></a>

### `isr_register`

```c
shared_irq_register_t shared_irq_driver_api::isr_register
```

本数据类型文档由以下文件生成：

- `zephyr/shared_irq.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/shared_irq.h](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h_source.html)
- [shared_irq_register_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#ae400920b45bedf3da66831597ebca841)
- [shared_irq_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#a0ff7a6ee448eb3e889aa9a7bd63e49bc)
- [shared_irq_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html#a22cf2ce082fea27f2087cd1abd74934c)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_secure_storage_its_uid_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_shared_vector_desc_t_结构体.md)
