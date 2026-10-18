---
id: learning.zephyr-docs.networking.page-123
title: DSA分布式交换机示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/ethernet/dsa/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_DSA分布式交换机示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ethernet/dsa/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

本示例用于测试和调试分布式交换机架构（Distributed Switch Architecture，DSA）。

源码位于 [`samples/net/ethernet/dsa`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/dsa)，可[在 GitHub 查看官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ethernet/dsa/README.rst/..)。

## 2. 前提条件（Requirements）

先按照[与主机系统联网](P007_与主机系统联网.md#networking-with-host)准备连接。

## 3. 构建和运行（Building and Running）

使用下列命令构建 DSA 示例：

```sh
west build -b <board to use> samples/net/ethernet/dsa -- -DCONF_FILE=prj.conf
```

> 译注——操作前提：在已准备好构建工具链与依赖的终端中，从 Zephyr 源码根目录执行；把 `<board to use>` 换成支持相应交换机及驱动的实际板目标。示例目录和 `prj.conf` 是官方源码已有文件。原页面只给出构建命令，设备运行、连接与驱动配置仍需按目标板文档完成，不能把构建成功直接记为交换机验证通过。

## 4. 另请参阅（See Also）

[分布式交换机架构（DSA）](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html)。


<a id="dsa"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P122_以太网服务质量示例.md) · [返回大纲](大纲.md) · [下一章](P124_TSN交换机示例.md)
