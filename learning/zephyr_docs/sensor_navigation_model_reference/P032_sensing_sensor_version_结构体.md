---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-32
title: sensing_sensor_version_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__version.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_sensing\_sensor\_version\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__version.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器版本（Sensor Version）。

```c
#include <zephyr/sensing/sensing.h>
```

<a id="details"></a>

传感器版本（Sensor Version）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a252f2958a116af20f6e02495f90d7f0f"></a>

```c
uint32_t value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[value](#a0023cbb5114f4a3d3a1cf388e5034cfc)。

以 32 位数值表示的版本。

```c
struct {
```

<a id="r_a3b23126d22889e5c045827b357778433"></a>

```c
uint8_t major
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[major](#ad7275123dd08f06ee0307325c8f5fb37)。

主版本号（major version）。

<a id="r_a47989a73ff9f1fe7cb267dc0cc82e69f"></a>

```c
uint8_t minor
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[minor](#a8d41ea3c181c7062aa8f76b17c652b41)。

次版本号（minor version）。

<a id="r_abf860222e2ec81746ea7dc4873c6c639"></a>

```c
uint8_t hotfix
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hotfix](#a10fe885cd0cd9a6a5209308e188def3d)。

热修复版本号（hotfix version）。

<a id="r_a2d0a35fd86181a4f6d738865400f79b3"></a>

```c
uint8_t build
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[build](#a668f5d23171c38e1cc13a4221e639815)。

构建版本号（build version）。

<a id="r_acb81a7ebae8f88e3b03595cadeae07ee"></a>

```c
}
```

<a id="r_a1c51022dff29bcc4fbc4b984ab72a48b"></a>

```c
};
```

可作为整体数值表示的版本，也可拆分为各独立字段。

## 32.2\_详细说明（Detailed Documentation）

<a id="a1c51022dff29bcc4fbc4b984ab72a48b"></a>

### `[union]`

```c
union { ... } sensing_sensor_version
```

可作为整体数值表示的版本，也可拆分为各独立字段。

<a id="a668f5d23171c38e1cc13a4221e639815"></a>

### `build`

```c
uint8_t sensing_sensor_version::build
```

构建版本号（build version）。

<a id="a10fe885cd0cd9a6a5209308e188def3d"></a>

### `hotfix`

```c
uint8_t sensing_sensor_version::hotfix
```

热修复版本号（hotfix version）。

<a id="ad7275123dd08f06ee0307325c8f5fb37"></a>

### `major`

```c
uint8_t sensing_sensor_version::major
```

主版本号（major version）。

<a id="a8d41ea3c181c7062aa8f76b17c652b41"></a>

### `minor`

```c
uint8_t sensing_sensor_version::minor
```

次版本号（minor version）。

<a id="a0023cbb5114f4a3d3a1cf388e5034cfc"></a>

### `value`

```c
uint32_t sensing_sensor_version::value
```

以 32 位数值表示的版本。

本数据类型文档由以下文件生成：

- `zephyr/sensing/sensing.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sensing_sensor_version](P032_sensing_sensor_version_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_sensing_sensor_value_uint32_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_sensor_byte_data_结构体.md)
