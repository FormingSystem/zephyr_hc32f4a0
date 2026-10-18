---
id: learning.zephyr-docs.boot-control-reference.page-5
title: MCUboot版本一镜像头结构
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcuboot__img__header__v1.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_MCUboot版本一镜像头结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcuboot__img__header__v1.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入MCUboot镜像控制、系统重启、内核版本和启动模式参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

版本 1 的 MCUboot 镜像头模型（Image Header Model）。

```c
#include <zephyr/dfu/mcuboot.h>
```

<a id="details"></a>

版本 1 的 MCUboot 镜像头模型。此结构表示版本 1 镜像头格式中的数据；头部中当前与应用无关的部分信息已省略。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a83a042079d850f383eef7a46cad14fa4"></a>

```c
uint32_t image_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[image_size](#a83a042079d850f383eef7a46cad14fa4)。

镜像大小，单位为字节（Bytes）。

<a id="r_a01dd3b50bb00accf4108b08c01df4e2b"></a>

```c
struct mcuboot_img_sem_ver sem_ver
```

相关声明：[mcuboot_img_sem_ver](P004_MCUboot语义版本结构.md)、[sem_ver](#a01dd3b50bb00accf4108b08c01df4e2b)。

镜像版本（Image Version）。

## 5.2\_详细说明（Detailed Documentation）

<a id="a83a042079d850f383eef7a46cad14fa4"></a>

### `image_size`

```c
uint32_t mcuboot_img_header_v1::image_size
```

镜像大小，单位为字节（Bytes）。

<a id="a01dd3b50bb00accf4108b08c01df4e2b"></a>

### `sem_ver`

```c
struct mcuboot_img_sem_ver mcuboot_img_header_v1::sem_ver
```

镜像版本（Image Version）。

## 5.3\_源码定位与版本边界

相对源码定位：[include/zephyr/dfu/mcuboot.h](../../../include/zephyr/dfu/mcuboot.h)、[subsys/dfu/boot/mcuboot.c](../../../subsys/dfu/boot/mcuboot.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。源码定位采用相对链接；本地版本如有差异，应核对来源摘要与实际实现，不把文档核对视为固件升级或重启实测。

> 译注——源码核对：公开镜像头结构是解码后的应用模型，包含版本标记与联合体，不是原始Flash镜像头。读取前应提供足够的结构大小，成功后先检查mcuboot_version，再访问对应的h成员；当前实现仅填充h.v1。

> 译注——源码核对：本次解码函数把mcuboot_version设为1以表示所支持的镜像头模型，并不查询正在运行的引导加载程序的完整发行版本。官方关于1.x.y的文字按原文保留；不得由此字段反推出设备安装的MCUboot精确版本。image_size表示从原始头解码得到的镜像大小，不是整个Flash分区容量。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [zephyr/dfu/mcuboot.h](P003_MCUboot头文件源码.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mcuboot_img_sem_ver](P004_MCUboot语义版本结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_MCUboot语义版本结构.md) · [返回大纲](大纲.md) · [下一章](P006_MCUboot镜像头结构.md)
