---
id: learning.zephyr-docs.cmake-reference.module.configuration_files
title: configuration_files
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/configuration_files.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_configuration_files

原文：[configuration_files](https://docs.zephyrproject.org/latest/build/cmake-ref/module/configuration_files.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:configuration_files"></a>

定位要使用的 Kconfig 和设备树（Devicetree，DT）配置文件，同时定位适当的应用配置目录（Application Configuration Directory）。

## 4.1\_变量（Variables）

本 CMake 模块完成后定义以下变量：

- [CONF_FILE](P035_CONF_FILE.md)。
- [EXTRA_CONF_FILE](P039_EXTRA_CONF_FILE.md)。
- [DTC_OVERLAY_FILE](P037_DTC_OVERLAY_FILE.md)。
- [EXTRA_DTC_OVERLAY_FILE](P040_EXTRA_DTC_OVERLAY_FILE.md)。
- [DTS_EXTRA_CPPFLAGS](P038_DTS_EXTRA_CPPFLAGS.md)。
- [APPLICATION_CONFIG_DIR](P021_APPLICATION_CONFIG_DIR.md)。

加载本模块时，如果上述变量已经设置，则不会更改它。模块设置的其他未列出变量仅供内部使用，可能不经提前通知就被删除、重命名或改变用途。

## 4.2\_原文相关链接

- [variable:CONF_FILE](P035_CONF_FILE.md#variable:CONF_FILE)
- [variable:EXTRA_CONF_FILE](P039_EXTRA_CONF_FILE.md#variable:EXTRA_CONF_FILE)
- [variable:DTC_OVERLAY_FILE](P037_DTC_OVERLAY_FILE.md#variable:DTC_OVERLAY_FILE)
- [variable:EXTRA_DTC_OVERLAY_FILE](P040_EXTRA_DTC_OVERLAY_FILE.md#variable:EXTRA_DTC_OVERLAY_FILE)
- [variable:DTS_EXTRA_CPPFLAGS](P038_DTS_EXTRA_CPPFLAGS.md#variable:DTS_EXTRA_CPPFLAGS)
- [variable:APPLICATION_CONFIG_DIR](P021_APPLICATION_CONFIG_DIR.md#variable:APPLICATION_CONFIG_DIR)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：boards](P003_boards.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：soc](P005_soc.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P003_boards.md) · [返回大纲](大纲.md) · [下一章](P005_soc.md)

</details>

<!-- reading-navigation:end -->
