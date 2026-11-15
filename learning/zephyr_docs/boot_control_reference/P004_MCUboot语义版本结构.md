---
id: learning.zephyr-docs.boot-control-reference.page-4
title: MCUboot语义版本结构
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcuboot__img__sem__ver.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_MCUboot语义版本结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcuboot__img__sem__ver.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入MCUboot镜像控制、系统重启、内核版本和启动模式参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

MCUboot 镜像头中的镜像版本表示。

```c
#include <zephyr/dfu/mcuboot.h>
```

<a id="details"></a>

MCUboot 镜像头中的镜像版本表示。MCUboot 固件镜像头内嵌一个采用语义版本格式（Semantic Versioning Format）的版本号；此结构表示其中包含的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_ae6fa8e6cc51e57e24a2d99670e543998"></a>

```c
uint8_t major
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[major](#ae6fa8e6cc51e57e24a2d99670e543998)。

<a id="r_a3ab711b800ab894e201d175b491a9552"></a>

```c
uint8_t minor
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[minor](#a3ab711b800ab894e201d175b491a9552)。

<a id="r_aabecc9fffb8ec7a7f02f2894f8d6e0f0"></a>

```c
uint16_t revision
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[revision](#aabecc9fffb8ec7a7f02f2894f8d6e0f0)。

<a id="r_abf2e489560daefaa0c5d33e9c7535dab"></a>

```c
uint32_t build_num
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[build_num](#abf2e489560daefaa0c5d33e9c7535dab)。

## 4.2\_详细说明（Detailed Documentation）

<a id="abf2e489560daefaa0c5d33e9c7535dab"></a>

### `build_num`

```c
uint32_t mcuboot_img_sem_ver::build_num
```

<a id="ae6fa8e6cc51e57e24a2d99670e543998"></a>

### `major`

```c
uint8_t mcuboot_img_sem_ver::major
```

<a id="a3ab711b800ab894e201d175b491a9552"></a>

### `minor`

```c
uint8_t mcuboot_img_sem_ver::minor
```

<a id="aabecc9fffb8ec7a7f02f2894f8d6e0f0"></a>

### `revision`

```c
uint16_t mcuboot_img_sem_ver::revision
```

## 4.3\_源码定位与版本边界

相对源码定位：[include/zephyr/dfu/mcuboot.h](../../../include/zephyr/dfu/mcuboot.h)、[subsys/dfu/boot/mcuboot.c](../../../subsys/dfu/boot/mcuboot.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。源码定位采用相对链接；本地版本如有差异，应核对来源摘要与实际实现，不把文档核对视为固件升级或重启实测。

> 译注——源码核对：镜像语义版本（Image Semantic Version）包含8位major、8位minor、16位revision和32位build_num。它与Zephyr内核版本的三个8位分量是不同格式；尤其不能用SYS_KERNEL_VER_*宏解析此结构。

> 译注——源码核对：此结构表达从镜像头取得的版本信息，不提供排序、兼容性判断或安全回滚策略。BOOT_IMG_VER_STRLEN_MAX为25，头文件注释按各分量十进制最大值与结尾空字符展示容量。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.4\_原页交叉引用（Cross References）

- [zephyr/dfu/mcuboot.h](P003_MCUboot头文件源码.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_MCUboot头文件源码.md) · [返回大纲](大纲.md) · [下一章](P005_MCUboot版本一镜像头结构.md)
