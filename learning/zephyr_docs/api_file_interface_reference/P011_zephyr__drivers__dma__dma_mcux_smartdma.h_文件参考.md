---
id: learning.zephyr-docs.api-file-interface-reference.page-11
title: zephyr__drivers__dma__dma_mcux_smartdma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__smartdma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_dma\_\_dma\_mcux\_smartdma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__smartdma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.1\_函数（Functions）

<a id="r_a72c469e163fc727135224893adbf757e"></a>

```c
void dma_smartdma_install_fw (const struct device *dev, uint8_t *firmware, uint32_t len)
```

相关声明：[dma_smartdma_install_fw](#a72c469e163fc727135224893adbf757e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

安装 SMARTDMA 固件（firmware）。

## 11.2\_详细说明（Detailed Documentation）

<a id="a72c469e163fc727135224893adbf757e"></a>

### `dma_smartdma_install_fw()`

```c
void dma_smartdma_install_fw ( const struct device * dev, uint8_t * firmware, uint32_t len )
```

安装 SMARTDMA 固件（firmware）。

为 smartDMA 安装自定义固件。此函数允许用户在 smartDMA 中安装自定义固件，其实现的 API 函数与标准 MCUX SDK 固件不同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | smartDMA 设备（device）。 |
| `firmware` | 包含 smartDMA 固件的缓冲区地址。 |
| `len` | 固件缓冲区的长度。 |


## 11.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P140_dma_mcux_smartdma.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_zephyr__bluetooth__mesh__dfu_metadata.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__drivers__dma__dma_silabs_ldma.h_文件参考.md)
