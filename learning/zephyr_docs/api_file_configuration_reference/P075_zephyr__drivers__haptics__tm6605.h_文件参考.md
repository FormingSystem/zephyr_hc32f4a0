---
id: learning.zephyr-docs.api-file-configuration-reference.page-75
title: zephyr__drivers__haptics__tm6605.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tm6605_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_zephyr\_\_drivers\_\_haptics\_\_tm6605.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tm6605_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

提供TM6605触觉反馈（Haptic）驱动API的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/haptics.h>
#include <zephyr/types.h>
```

查看此文件的源码。

提供TM6605触觉反馈（Haptic）驱动API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 75.1\_枚举（Enumerations）

<a id="r_ga8684b734f5192c0d22a3eddc4ca97d1e"></a>

```c
enum tm6605_effect { TM6605_EFFECT_SHARP_CLICK = 1 , TM6605_EFFECT_INSTANT_CLICK = 4 , TM6605_EFFECT_LIGHT_TAP = 7 , TM6605_EFFECT_DOUBLE_CLICK = 10 , TM6605_EFFECT_LIGHT_PULSE = 13 , TM6605_EFFECT_STRONG_ALERT = 14 , TM6605_EFFECT_MEDIUM_DURATION_ALERT = 15 , TM6605_EFFECT_SHARP_CLICK_2 = 17 , TM6605_EFFECT_MEDIUM_CLICK = 21 , TM6605_EFFECT_FLASH_STRIKE = 24 , TM6605_EFFECT_DOUBLE_HIGH_CLICK_SHORT = 27 , TM6605_EFFECT_DOUBLE_MEDIUM_CLICK_SHORT = 31 , TM6605_EFFECT_DOUBLE_FLASH_STRIKE_SHORT = 34 , TM6605_EFFECT_DOUBLE_INSTANT_CLICK_LONG = 37 , TM6605_EFFECT_DOUBLE_MEDIUM_INSTANT_CLICK_LONG = 41 , TM6605_EFFECT_DOUBLE_FLASH_STRIKE_LONG = 44 , TM6605_EFFECT_ALERT = 47 , TM6605_EFFECT_TOGGLE_CLICK = 58 , TM6605_EFFECT_LONG_SLOW_FADE_1 = 70 , TM6605_EFFECT_LONG_SLOW_FADE_2 = 71 , TM6605_EFFECT_MEDIUM_SLOW_FADE_1 = 72 , TM6605_EFFECT_MEDIUM_SLOW_FADE_2 = 73 , TM6605_EFFECT_SHORT_SLOW_FADE_1 = 74 , TM6605_EFFECT_SHORT_SLOW_FADE_2 = 75 , TM6605_EFFECT_LONG_FAST_FADE_1 = 76 , TM6605_EFFECT_LONG_FAST_FADE_2 = 77 , TM6605_EFFECT_MEDIUM_FAST_FADE_1 = 78 , TM6605_EFFECT_MEDIUM_FAST_FADE_2 = 79 , TM6605_EFFECT_SHORT_FAST_FADE_1 = 80 , TM6605_EFFECT_SHORT_FAST_FADE_2 = 81 , TM6605_EFFECT_LONG_SLOW_BOOST_1 = 82 , TM6605_EFFECT_LONG_SLOW_BOOST_2 = 83 , TM6605_EFFECT_MEDIUM_SLOW_BOOST_1 = 84 , TM6605_EFFECT_MEDIUM_SLOW_BOOST_2 = 85 , TM6605_EFFECT_SHORT_SLOW_BOOST_1 = 86 , TM6605_EFFECT_SHORT_SLOW_BOOST_2 = 87 , TM6605_EFFECT_LONG_FAST_BOOST_1 = 88 , TM6605_EFFECT_LONG_FAST_BOOST_2 = 89 , TM6605_EFFECT_MEDIUM_FAST_BOOST_1 = 90 , TM6605_EFFECT_MEDIUM_FAST_BOOST_2 = 91 , TM6605_EFFECT_SHORT_FAST_BOOST_1 = 92 , TM6605_EFFECT_SHORT_FAST_BOOST_2 = 93 , TM6605_EFFECT_LONG_ALERT = 118 , TM6605_EFFECT_SOFT_NOISE = 119 , TM6605_EFFECT_SLEEP_COMMAND = 123 }
```

相关声明：[tm6605_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#ga8684b734f5192c0d22a3eddc4ca97d1e)、[TM6605_EFFECT_SHARP_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea7245aa138e7d8ebed324080d3a3ed8f2)、[TM6605_EFFECT_INSTANT_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea7454cda64f24c189df318e699c57053d)、[TM6605_EFFECT_LIGHT_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaf5f28798fecb8d8aac7f55cce67ceb8e)、[TM6605_EFFECT_DOUBLE_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea6b61e9987fd24908b80d2e0f6d7b5b38)、[TM6605_EFFECT_LIGHT_PULSE](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea84ac6c09e9a89d803a21e8436330a99d)、[TM6605_EFFECT_STRONG_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ead587a1935c8834ef7954836ea086b8d0)、[TM6605_EFFECT_MEDIUM_DURATION_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea238fd287f033224c957a6c2f31fcf10d)、[TM6605_EFFECT_SHARP_CLICK_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eab13516e3548ebbddf5f31487db9aa09c)、[TM6605_EFFECT_MEDIUM_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea99773c2f6742cdef0dff592372a836d9)、[TM6605_EFFECT_FLASH_STRIKE](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ead7dfbdb828af6319c32ac07724983a18)、[TM6605_EFFECT_DOUBLE_HIGH_CLICK_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaeff0fa9e352ab86a6c893bdf8482ddd3)、[TM6605_EFFECT_DOUBLE_MEDIUM_CLICK_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea01884023003fe5390afb4bb50bc6299f)、[TM6605_EFFECT_DOUBLE_FLASH_STRIKE_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea4ba8728ccc89f15f45f53cca681209f3)、[TM6605_EFFECT_DOUBLE_INSTANT_CLICK_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea2f7a7bdbc253232e7ee92f3c20b46966)、[TM6605_EFFECT_DOUBLE_MEDIUM_INSTANT_CLICK_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea0fe8ae7b85a290979a348dc4d15fd4b2)、[TM6605_EFFECT_DOUBLE_FLASH_STRIKE_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaae424b24471abdc1f0372039823c2ff5)、[TM6605_EFFECT_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea4bc0dff942235c620a33b942ae38ccb8)、[TM6605_EFFECT_TOGGLE_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea480c408df6b0609f757fe7b21b91e470)、[TM6605_EFFECT_LONG_SLOW_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea1a41117a37ea22375f2dc85679d155d6)、[TM6605_EFFECT_LONG_SLOW_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea1fa146ddc6939dfa0feb03fa8762ecd4)、[TM6605_EFFECT_MEDIUM_SLOW_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea900dfd8638cee1e53d957cd5fb21b5e8)、[TM6605_EFFECT_MEDIUM_SLOW_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eab4b228e4d573b91ef4a489c4bdd54902)、[TM6605_EFFECT_SHORT_SLOW_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea22c031294a06d3f46f78abf09c62fe4e)、[TM6605_EFFECT_SHORT_SLOW_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eacfc279fab21fa9d24c8411b33aab217d)、[TM6605_EFFECT_LONG_FAST_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ead144506b7180bce8895f85cf3d7ccf76)、[TM6605_EFFECT_LONG_FAST_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea5fe8229e028627a5177780f5cdbb9235)、[TM6605_EFFECT_MEDIUM_FAST_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea8f77b5fba334fb453343ad63a4bf563f)、[TM6605_EFFECT_MEDIUM_FAST_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ead359f1f092187175f85d233241740ad4)、[TM6605_EFFECT_SHORT_FAST_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaccde26d04d802ce9a4604c518dd348d4)、[TM6605_EFFECT_SHORT_FAST_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaa84402bccf42fe5cc58c542a52384621)、[TM6605_EFFECT_LONG_SLOW_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea982ec7e1f05d526ab8b8b4915f2bc103)、[TM6605_EFFECT_LONG_SLOW_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea4188d53bf86b87ad6d4c7e9c98e23da7)、[TM6605_EFFECT_MEDIUM_SLOW_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eacb0971d5281c844362cd2ec170cd5382)、[TM6605_EFFECT_MEDIUM_SLOW_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea1f1ef0739cb97f52f55d6bfa3a488820)、[TM6605_EFFECT_SHORT_SLOW_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea4f7fbea457dc0433598fbf6f024f1fea)、[TM6605_EFFECT_SHORT_SLOW_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea42fe98945cb27bca94a61a8844845010)、[TM6605_EFFECT_LONG_FAST_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea0cffc315ea1af5594e939b7976611afe)、[TM6605_EFFECT_LONG_FAST_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eafef3a7f71e26d57be5b09f80177d1a2e)、[TM6605_EFFECT_MEDIUM_FAST_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea76528a47fb9582c4cee744356b37ec3e)、[TM6605_EFFECT_MEDIUM_FAST_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea700dc1fff7268084bf9f04819d60f645)、[TM6605_EFFECT_SHORT_FAST_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eab42d3d5e6a3e41a2eb7cb637330bcb33)、[TM6605_EFFECT_SHORT_FAST_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eac88cfb69b4cdd982b2eeca9ce58d4a66)、[TM6605_EFFECT_LONG_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaa80e817931e4d20dbc3e01d877f8dc17)、[TM6605_EFFECT_SOFT_NOISE](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea1e7e70244ae3981a3883c4224237b0bb)、[TM6605_EFFECT_SLEEP_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea13e5302f47b219021b79579f9d1ade66)。

TM6605 预编程效果标识（Pre-Programmed Effect IDs）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 75.2\_函数（Functions）

<a id="r_gaf326d73989542f4f65542ce2060e2fe0"></a>

```c
int tm6605_select_effect (const struct device *dev, enum tm6605_effect effect)
```

相关声明：[tm6605_select_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gaf326d73989542f4f65542ce2060e2fe0)、[device](../device_reference/P002_设备对象结构.md)、[tm6605_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#ga8684b734f5192c0d22a3eddc4ca97d1e)。

选择下一次调用 `start_output` 时播放的触觉效果（Haptic Effect）。


## 75.3\_原页交叉引用（Cross References）

- [zephyr/drivers/haptics.h](https://docs.zephyrproject.org/latest/doxygen/html/haptics_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P227_tm6605.h_源码浏览.md)
- [tm6605_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#ga8684b734f5192c0d22a3eddc4ca97d1e)
- [TM6605_EFFECT_SHARP_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea7245aa138e7d8ebed324080d3a3ed8f2)
- [TM6605_EFFECT_INSTANT_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea7454cda64f24c189df318e699c57053d)
- [TM6605_EFFECT_LIGHT_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaf5f28798fecb8d8aac7f55cce67ceb8e)
- [TM6605_EFFECT_DOUBLE_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea6b61e9987fd24908b80d2e0f6d7b5b38)
- [TM6605_EFFECT_LIGHT_PULSE](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea84ac6c09e9a89d803a21e8436330a99d)
- [TM6605_EFFECT_STRONG_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ead587a1935c8834ef7954836ea086b8d0)
- [TM6605_EFFECT_MEDIUM_DURATION_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea238fd287f033224c957a6c2f31fcf10d)
- [TM6605_EFFECT_SHARP_CLICK_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eab13516e3548ebbddf5f31487db9aa09c)
- [TM6605_EFFECT_MEDIUM_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea99773c2f6742cdef0dff592372a836d9)
- [TM6605_EFFECT_FLASH_STRIKE](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ead7dfbdb828af6319c32ac07724983a18)
- [TM6605_EFFECT_DOUBLE_HIGH_CLICK_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaeff0fa9e352ab86a6c893bdf8482ddd3)
- [TM6605_EFFECT_DOUBLE_MEDIUM_CLICK_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea01884023003fe5390afb4bb50bc6299f)
- [TM6605_EFFECT_DOUBLE_FLASH_STRIKE_SHORT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea4ba8728ccc89f15f45f53cca681209f3)
- [TM6605_EFFECT_DOUBLE_INSTANT_CLICK_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea2f7a7bdbc253232e7ee92f3c20b46966)
- [TM6605_EFFECT_DOUBLE_MEDIUM_INSTANT_CLICK_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea0fe8ae7b85a290979a348dc4d15fd4b2)
- [TM6605_EFFECT_DOUBLE_FLASH_STRIKE_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaae424b24471abdc1f0372039823c2ff5)
- [TM6605_EFFECT_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea4bc0dff942235c620a33b942ae38ccb8)
- [TM6605_EFFECT_TOGGLE_CLICK](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea480c408df6b0609f757fe7b21b91e470)
- [TM6605_EFFECT_LONG_SLOW_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea1a41117a37ea22375f2dc85679d155d6)
- [TM6605_EFFECT_LONG_SLOW_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea1fa146ddc6939dfa0feb03fa8762ecd4)
- [TM6605_EFFECT_MEDIUM_SLOW_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea900dfd8638cee1e53d957cd5fb21b5e8)
- [TM6605_EFFECT_MEDIUM_SLOW_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eab4b228e4d573b91ef4a489c4bdd54902)
- [TM6605_EFFECT_SHORT_SLOW_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea22c031294a06d3f46f78abf09c62fe4e)
- [TM6605_EFFECT_SHORT_SLOW_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eacfc279fab21fa9d24c8411b33aab217d)
- [TM6605_EFFECT_LONG_FAST_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ead144506b7180bce8895f85cf3d7ccf76)
- [TM6605_EFFECT_LONG_FAST_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea5fe8229e028627a5177780f5cdbb9235)
- [TM6605_EFFECT_MEDIUM_FAST_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea8f77b5fba334fb453343ad63a4bf563f)
- [TM6605_EFFECT_MEDIUM_FAST_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ead359f1f092187175f85d233241740ad4)
- [TM6605_EFFECT_SHORT_FAST_FADE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaccde26d04d802ce9a4604c518dd348d4)
- [TM6605_EFFECT_SHORT_FAST_FADE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaa84402bccf42fe5cc58c542a52384621)
- [TM6605_EFFECT_LONG_SLOW_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea982ec7e1f05d526ab8b8b4915f2bc103)
- [TM6605_EFFECT_LONG_SLOW_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea4188d53bf86b87ad6d4c7e9c98e23da7)
- [TM6605_EFFECT_MEDIUM_SLOW_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eacb0971d5281c844362cd2ec170cd5382)
- [TM6605_EFFECT_MEDIUM_SLOW_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea1f1ef0739cb97f52f55d6bfa3a488820)
- [TM6605_EFFECT_SHORT_SLOW_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea4f7fbea457dc0433598fbf6f024f1fea)
- [TM6605_EFFECT_SHORT_SLOW_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea42fe98945cb27bca94a61a8844845010)
- [TM6605_EFFECT_LONG_FAST_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea0cffc315ea1af5594e939b7976611afe)
- [TM6605_EFFECT_LONG_FAST_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eafef3a7f71e26d57be5b09f80177d1a2e)
- [TM6605_EFFECT_MEDIUM_FAST_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea76528a47fb9582c4cee744356b37ec3e)
- [TM6605_EFFECT_MEDIUM_FAST_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea700dc1fff7268084bf9f04819d60f645)
- [TM6605_EFFECT_SHORT_FAST_BOOST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eab42d3d5e6a3e41a2eb7cb637330bcb33)
- [TM6605_EFFECT_SHORT_FAST_BOOST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eac88cfb69b4cdd982b2eeca9ce58d4a66)
- [TM6605_EFFECT_LONG_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1eaa80e817931e4d20dbc3e01d877f8dc17)
- [TM6605_EFFECT_SOFT_NOISE](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea1e7e70244ae3981a3883c4224237b0bb)
- [TM6605_EFFECT_SLEEP_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gga8684b734f5192c0d22a3eddc4ca97d1ea13e5302f47b219021b79579f9d1ade66)
- [tm6605_select_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__tm6605__interface.html#gaf326d73989542f4f65542ce2060e2fe0)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P074_zephyr__drivers__led_strip__tlc5971.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P076_zephyr__drivers__uart_emul.h_文件参考.md)
