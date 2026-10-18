---
id: learning.zephyr-docs.boards-espressif.page-15
title: Binary Blobs
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/system-requirements.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="binary-blobs"></a>

# 第15章\_二进制组件（Binary Blobs）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/system-requirements.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Espressif 硬件抽象层（HAL）需要射频（RF）二进制组件才能工作。运行下面的命令获取这些文件。

```text
west blobs fetch hal_espressif
```

注意（Note）

建议在 `west update` 之后运行上述命令。

---

[上一章](P014_ESP32-S3_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_ESP32-DevKitC.md)
