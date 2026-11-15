---
id: learning.zephyr-docs.platform-security-model-reference.page-74
title: vtd_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvtd__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_vtd\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvtd__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/interrupt_controller/intel_vtd.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 74.1\_数据成员（Data Fields）

<a id="r_a3177c806bd86ebe4dc6c94141c9d5f04"></a>

```c
vtd_alloc_entries_f allocate_entries
```

相关声明：[vtd_alloc_entries_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a3bded96a42bec41476ff6bc9f75676b4)、[allocate_entries](#a3177c806bd86ebe4dc6c94141c9d5f04)。

<a id="r_a97f93762584ea000a149ded0d726a993"></a>

```c
vtd_remap_msi_f remap_msi
```

相关声明：[vtd_remap_msi_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#aadb69e257884026693109510e20dc2b4)、[remap_msi](#a97f93762584ea000a149ded0d726a993)。

<a id="r_ac03cd6690017568b51d1b4bedd1fea09"></a>

```c
vtd_remap_f remap
```

相关声明：[vtd_remap_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#afefa59b2064053d90445127da9b64bfb)、[remap](#ac03cd6690017568b51d1b4bedd1fea09)。

<a id="r_a03236811cfc87b4653ba1a2f53bc50a1"></a>

```c
vtd_set_irte_vector_f set_irte_vector
```

相关声明：[vtd_set_irte_vector_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a06190d6273d0adeb92e9e4e4fa79d9b4)、[set_irte_vector](#a03236811cfc87b4653ba1a2f53bc50a1)。

<a id="r_a39157ec0077a20a900bbe19f3cc8d1b1"></a>

```c
vtd_get_irte_by_vector_f get_irte_by_vector
```

相关声明：[vtd_get_irte_by_vector_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a944bfa2dc643fd3ff182eee12d836ae5)、[get_irte_by_vector](#a39157ec0077a20a900bbe19f3cc8d1b1)。

<a id="r_ac67dacb59216e44e55c832a26b87854f"></a>

```c
vtd_get_irte_vector_f get_irte_vector
```

相关声明：[vtd_get_irte_vector_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#af3ddf5e22fcb4956e4887e1982fae28e)、[get_irte_vector](#ac67dacb59216e44e55c832a26b87854f)。

<a id="r_acc5af4aaaeed8abb8768d21767c67c58"></a>

```c
vtd_set_irte_irq_f set_irte_irq
```

相关声明：[vtd_set_irte_irq_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a63733309814847ba4204776e8ace9a85)、[set_irte_irq](#acc5af4aaaeed8abb8768d21767c67c58)。

<a id="r_adf1c688b60ef445581dee2344a48c8b6"></a>

```c
vtd_get_irte_by_irq_f get_irte_by_irq
```

相关声明：[vtd_get_irte_by_irq_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a0a2e483fe9159a46d6265b257841f43a)、[get_irte_by_irq](#adf1c688b60ef445581dee2344a48c8b6)。

<a id="r_ac2fbdcfe7bcb0c9ef548aefe1c80b96b"></a>

```c
vtd_set_irte_msi_f set_irte_msi
```

相关声明：[vtd_set_irte_msi_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a0118f224100f721a508ce00c3ae99698)、[set_irte_msi](#ac2fbdcfe7bcb0c9ef548aefe1c80b96b)。

<a id="r_aac4ab98b9bf8a557cec22c685433888c"></a>

```c
vtd_irte_is_msi_f irte_is_msi
```

相关声明：[vtd_irte_is_msi_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a622083e8841c3899ca7b7156f526581f)、[irte_is_msi](#aac4ab98b9bf8a557cec22c685433888c)。

## 74.2\_详细说明（Detailed Documentation）

<a id="a3177c806bd86ebe4dc6c94141c9d5f04"></a>

### `allocate_entries`

```c
vtd_alloc_entries_f vtd_driver_api::allocate_entries
```

<a id="adf1c688b60ef445581dee2344a48c8b6"></a>

### `get_irte_by_irq`

```c
vtd_get_irte_by_irq_f vtd_driver_api::get_irte_by_irq
```

<a id="a39157ec0077a20a900bbe19f3cc8d1b1"></a>

### `get_irte_by_vector`

```c
vtd_get_irte_by_vector_f vtd_driver_api::get_irte_by_vector
```

<a id="ac67dacb59216e44e55c832a26b87854f"></a>

### `get_irte_vector`

```c
vtd_get_irte_vector_f vtd_driver_api::get_irte_vector
```

<a id="aac4ab98b9bf8a557cec22c685433888c"></a>

### `irte_is_msi`

```c
vtd_irte_is_msi_f vtd_driver_api::irte_is_msi
```

<a id="ac03cd6690017568b51d1b4bedd1fea09"></a>

### `remap`

```c
vtd_remap_f vtd_driver_api::remap
```

<a id="a97f93762584ea000a149ded0d726a993"></a>

### `remap_msi`

```c
vtd_remap_msi_f vtd_driver_api::remap_msi
```

<a id="acc5af4aaaeed8abb8768d21767c67c58"></a>

### `set_irte_irq`

```c
vtd_set_irte_irq_f vtd_driver_api::set_irte_irq
```

<a id="ac2fbdcfe7bcb0c9ef548aefe1c80b96b"></a>

### `set_irte_msi`

```c
vtd_set_irte_msi_f vtd_driver_api::set_irte_msi
```

<a id="a03236811cfc87b4653ba1a2f53bc50a1"></a>

### `set_irte_vector`

```c
vtd_set_irte_vector_f vtd_driver_api::set_irte_vector
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/interrupt_controller/intel_vtd.h`

## 74.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/intel_vtd.h](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h_source.html)
- [vtd_alloc_entries_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a3bded96a42bec41476ff6bc9f75676b4)
- [vtd_remap_msi_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#aadb69e257884026693109510e20dc2b4)
- [vtd_remap_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#afefa59b2064053d90445127da9b64bfb)
- [vtd_set_irte_vector_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a06190d6273d0adeb92e9e4e4fa79d9b4)
- [vtd_get_irte_by_vector_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a944bfa2dc643fd3ff182eee12d836ae5)
- [vtd_get_irte_vector_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#af3ddf5e22fcb4956e4887e1982fae28e)
- [vtd_set_irte_irq_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a63733309814847ba4204776e8ace9a85)
- [vtd_get_irte_by_irq_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a0a2e483fe9159a46d6265b257841f43a)
- [vtd_set_irte_msi_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a0118f224100f721a508ce00c3ae99698)
- [vtd_irte_is_msi_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a622083e8841c3899ca7b7156f526581f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P073_vector_desc_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P075_xen_domctl_pt_irq_结构体.md)
