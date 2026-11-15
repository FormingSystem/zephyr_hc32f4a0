---
id: learning.zephyr-docs.boot-control-reference.page-6
title: MCUboot镜像头结构
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcuboot__img__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_MCUboot镜像头结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcuboot__img__header.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入MCUboot镜像控制、系统重启、内核版本和启动模式参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

MCUboot 镜像头模型。

```c
#include <zephyr/dfu/mcuboot.h>
```

<a id="details"></a>

MCUboot 镜像头模型。它包含解码后的镜像头，以及构建该镜像头所针对的 MCUboot 主版本号。（MCUboot 项目保证：对镜像头作不兼容修改时，引导加载程序自身的主版本号也会改变，并且能够从镜像头的持久化表示中检测出来。）

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_ab5147e9586062d4dd5b381af13f1e82d"></a>

```c
uint32_t mcuboot_version
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mcuboot_version](#ab5147e9586062d4dd5b381af13f1e82d)。

此镜像头面向的 MCUboot 版本。

```c
union {
```

<a id="r_a87cab9545e5b8e8a85f244554334a8af"></a>

```c
struct mcuboot_img_header_v1 v1
```

相关声明：[mcuboot_img_header_v1](P005_MCUboot版本一镜像头结构.md)、[v1](#aff12aff412ea774f96948e7db0b25009)。

MCUboot 版本 1 的镜像头信息。

<a id="r_a34f5595bbd5b974c04386b568c88e39f"></a>

```c
} h
```

相关声明：[h](#a34f5595bbd5b974c04386b568c88e39f)。

镜像头信息。

## 6.2\_详细说明（Detailed Documentation）

<a id="a34f5595bbd5b974c04386b568c88e39f"></a>

### `[union]`

```c
union { ... } mcuboot_img_header::h
```

镜像头信息。

只能访问与上述 `mcuboot_version` 字段相对应的联合体成员（Union Member）中的字段。

<a id="ab5147e9586062d4dd5b381af13f1e82d"></a>

### `mcuboot_version`

```c
uint32_t mcuboot_img_header::mcuboot_version
```

此镜像头面向的 MCUboot 版本。

值 1 对应 MCUboot 版本 1.x.y。

<a id="aff12aff412ea774f96948e7db0b25009"></a>

### `v1`

```c
struct mcuboot_img_header_v1 mcuboot_img_header::v1
```

MCUboot 版本 1 的镜像头信息。

## 6.3\_源码定位与版本边界

相对源码定位：[include/zephyr/dfu/mcuboot.h](../../../include/zephyr/dfu/mcuboot.h)、[subsys/dfu/boot/mcuboot.c](../../../subsys/dfu/boot/mcuboot.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。源码定位采用相对链接；本地版本如有差异，应核对来源摘要与实际实现，不把文档核对视为固件升级或重启实测。

> 译注——源码核对：公开镜像头结构是解码后的应用模型，包含版本标记与联合体，不是原始Flash镜像头。读取前应提供足够的结构大小，成功后先检查mcuboot_version，再访问对应的h成员；当前实现仅填充h.v1。

> 译注——源码核对：本次解码函数把mcuboot_version设为1以表示所支持的镜像头模型，并不查询正在运行的引导加载程序的完整发行版本。官方关于1.x.y的文字按原文保留；不得由此字段反推出设备安装的MCUboot精确版本。image_size表示从原始头解码得到的镜像大小，不是整个Flash分区容量。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.4\_原页交叉引用（Cross References）

- [zephyr/dfu/mcuboot.h](P003_MCUboot头文件源码.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mcuboot_img_header_v1](P005_MCUboot版本一镜像头结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_MCUboot版本一镜像头结构.md) · [返回大纲](大纲.md) · [下一章](P007_系统重启头文件参考.md)
