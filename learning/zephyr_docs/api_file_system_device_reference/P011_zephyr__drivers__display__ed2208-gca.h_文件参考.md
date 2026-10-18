---
id: learning.zephyr-docs.api-file-system-device-reference.page-11
title: zephyr__drivers__display__ed2208-gca.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ed2208-gca_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_display\_\_ed2208-gca.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ed2208-gca_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ED2208-GCA（EL073TF1）Spectra 6电子墨水显示器（E-Ink Display）的调色板定义。

<a id="details"></a>

```c
#include <zephyr/drivers/display.h>
```

查看此文件的源码。

ED2208-GCA（EL073TF1）Spectra 6电子墨水显示器（E-Ink Display）的调色板定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="define-members-0"></a>

### ED2208-GCA（EL073TF1）颜色定义（Color Definitions）

<a id="r_ga67dc44a48a9290447856ea5ca28d8439"></a>

```c
#define ED2208_GCA_COLOR_BLACK 0x00
```

相关声明：[ED2208_GCA_COLOR_BLACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga67dc44a48a9290447856ea5ca28d8439)。

黑色索引（Black color index）。

<a id="r_ga33d53105e77d0669148111c22e37dc70"></a>

```c
#define ED2208_GCA_COLOR_WHITE 0x01
```

相关声明：[ED2208_GCA_COLOR_WHITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga33d53105e77d0669148111c22e37dc70)。

白色索引（White color index）。

<a id="r_gaaac429b04da8a2c3c3d6ae6583b85de7"></a>

```c
#define ED2208_GCA_COLOR_YELLOW 0x02
```

相关声明：[ED2208_GCA_COLOR_YELLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#gaaac429b04da8a2c3c3d6ae6583b85de7)。

黄色索引（Yellow color index）。

<a id="r_ga6887c0ee4a6e683a0ad4cdad2547db9a"></a>

```c
#define ED2208_GCA_COLOR_RED 0x03
```

相关声明：[ED2208_GCA_COLOR_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga6887c0ee4a6e683a0ad4cdad2547db9a)。

红色索引（Red color index）。

<a id="r_ga88671850b7a9954b918edc07fd27a541"></a>

```c
#define ED2208_GCA_COLOR_BLUE 0x05
```

相关声明：[ED2208_GCA_COLOR_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga88671850b7a9954b918edc07fd27a541)。

蓝色索引（Blue color index）。

<a id="r_ga8ea97937625cb32067e0bdd89ee20669"></a>

```c
#define ED2208_GCA_COLOR_GREEN 0x06
```

相关声明：[ED2208_GCA_COLOR_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga8ea97937625cb32067e0bdd89ee20669)。

绿色索引（Green color index）。

<a id="r_ga6069fc9215aba137fe0d9bf179a72b7f"></a>

```c
#define ED2208_GCA_COLOR_PALETTE_SIZE 7
```

相关声明：[ED2208_GCA_COLOR_PALETTE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga6069fc9215aba137fe0d9bf179a72b7f)。

调色板（palette）中的颜色数量，包括空槽位。


## 11.2\_原页交叉引用（Cross References）

- [zephyr/drivers/display.h](../api_source_supplement_reference/P041_display.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P218_ed2208-gca.h_源码浏览.md)
- [ED2208_GCA_COLOR_BLACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga67dc44a48a9290447856ea5ca28d8439)
- [ED2208_GCA_COLOR_WHITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga33d53105e77d0669148111c22e37dc70)
- [ED2208_GCA_COLOR_YELLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#gaaac429b04da8a2c3c3d6ae6583b85de7)
- [ED2208_GCA_COLOR_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga6887c0ee4a6e683a0ad4cdad2547db9a)
- [ED2208_GCA_COLOR_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga88671850b7a9954b918edc07fd27a541)
- [ED2208_GCA_COLOR_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga8ea97937625cb32067e0bdd89ee20669)
- [ED2208_GCA_COLOR_PALETTE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ed2208__gca__display__interface.html#ga6069fc9215aba137fe0d9bf179a72b7f)

<a id="header-details"></a>

---

[上一章](P010_zephyr__dt-bindings__sensor__mtch9010.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__net__ethernet_bridge_fdb.h_文件参考.md)
