---
id: learning.zephyr-docs.api-file-reference.page-415
title: zephyr__drivers__video__stm32_dcmipp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第415章\_zephyr\_\_drivers\_\_video\_\_stm32\_dcmipp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 415.1\_函数（Functions）

<a id="r_a74db1fc75808b5d306f56a59539a3cab"></a>

```c
void stm32_dcmipp_isp_vsync_update (DCMIPP_HandleTypeDef *hdcmipp, uint32_t Pipe)
```

相关声明：[stm32_dcmipp_isp_vsync_update](#a74db1fc75808b5d306f56a59539a3cab)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a37286ed8041fa5de1840151a3d8c5a74"></a>

```c
int stm32_dcmipp_isp_init (DCMIPP_HandleTypeDef *hdcmipp, const struct device *source)
```

相关声明：[stm32_dcmipp_isp_init](#a37286ed8041fa5de1840151a3d8c5a74)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a3f46ac0646bb14656fcb89a7720d171a"></a>

```c
int stm32_dcmipp_isp_start (void)
```

相关声明：[stm32_dcmipp_isp_start](#a3f46ac0646bb14656fcb89a7720d171a)。

<a id="r_ac395f951a019d41ec3b72156cd6b5ce5"></a>

```c
int stm32_dcmipp_isp_stop (void)
```

相关声明：[stm32_dcmipp_isp_stop](#ac395f951a019d41ec3b72156cd6b5ce5)。

## 415.2\_详细说明（Detailed Documentation）

<a id="a37286ed8041fa5de1840151a3d8c5a74"></a>

### `stm32_dcmipp_isp_init()`

```c
int stm32_dcmipp_isp_init ( DCMIPP_HandleTypeDef * hdcmipp, const struct device * source )
```

<a id="a3f46ac0646bb14656fcb89a7720d171a"></a>

### `stm32_dcmipp_isp_start()`

```c
int stm32_dcmipp_isp_start ( void )
```

<a id="ac395f951a019d41ec3b72156cd6b5ce5"></a>

### `stm32_dcmipp_isp_stop()`

```c
int stm32_dcmipp_isp_stop ( void )
```

<a id="a74db1fc75808b5d306f56a59539a3cab"></a>

### `stm32_dcmipp_isp_vsync_update()`

```c
void stm32_dcmipp_isp_vsync_update ( DCMIPP_HandleTypeDef * hdcmipp, uint32_t Pipe )
```


## 415.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P188_stm32_dcmipp.h_源码浏览.md)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P414_zephyr__dt-bindings__input__stm32-tsc-defines.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P416_zephyr__dt-bindings__clock__stm32c0_clock.h_文件参考.md)
