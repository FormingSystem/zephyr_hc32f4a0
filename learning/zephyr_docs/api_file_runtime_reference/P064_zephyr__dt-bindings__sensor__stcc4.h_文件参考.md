---
id: learning.zephyr-docs.api-file-runtime-reference.page-64
title: zephyr__dt-bindings__sensor__stcc4.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stcc4_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_zephyr\_\_dt-bindings\_\_sensor\_\_stcc4.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stcc4_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Sensirion STCC4 CO2 sensor的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Sensirion STCC4 CO2 sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 64.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 测量模式（Measurement Mode）

设备树属性（Devicetree Property）`measurement-mode` 的取值。

<a id="r_ga7ea66c748fdf9063352690a70fd88d6f"></a>

```c
#define STCC4_DT_MODE_CONTINUOUS 0
```

相关声明：[STCC4_DT_MODE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__stcc4__interface.html#ga7ea66c748fdf9063352690a70fd88d6f)。

连续测量（Continuous Measurement），频率约为 1 Hz。

<a id="r_ga95c5d1bae8d0cbfa3f4d4c5c37de03d7"></a>

```c
#define STCC4_DT_MODE_SINGLE_SHOT 1
```

相关声明：[STCC4_DT_MODE_SINGLE_SHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__stcc4__interface.html#ga95c5d1bae8d0cbfa3f4d4c5c37de03d7)。

单次测量（Single-Shot Measurement），每次 500 ms。


## 64.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P819_stcc4.h_源码浏览.md)
- [STCC4_DT_MODE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__stcc4__interface.html#ga7ea66c748fdf9063352690a70fd88d6f)
- [STCC4_DT_MODE_SINGLE_SHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__stcc4__interface.html#ga95c5d1bae8d0cbfa3f4d4c5c37de03d7)

<a id="header-details"></a>

---

[上一章](P063_zephyr__mgmt__mcumgr__grp__stat_mgmt__stat_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P065_zephyr__drivers__stepper__stepper_tmcm3216.h_文件参考.md)
