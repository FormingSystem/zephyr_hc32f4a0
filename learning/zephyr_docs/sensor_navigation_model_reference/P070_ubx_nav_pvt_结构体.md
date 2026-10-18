---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-70
title: ubx_nav_pvt_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__nav__pvt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_ubx\_nav\_pvt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__nav__pvt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a1edd0fc359b863cf1cd1b3ddab9a279d"></a>

```c
uint32_t itow
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[itow](#a426086b12ff09fb8a00dd4623fea307e)。

<a id="r_a8d4cc7c7b642e829f1e4f4919f4614ee"></a>

```c
uint16_t year
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[year](#a84c6640806485f270b8d51d06cc49709)。

<a id="r_a9fa5d95f84425b2e30408df162d342ae"></a>

```c
uint8_t month
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[month](#ad90042dc5e00b91f004badcb0c3a5f4c)。

<a id="r_a79fc43e7a6612507b21f4a07d9409051"></a>

```c
uint8_t day
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[day](#aeadb05fe45a3a0539c899129e40059fd)。

<a id="r_ae4245064f580fcb1296e26c0f80ff2eb"></a>

```c
uint8_t hour
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hour](#aeb710663626935d21c77a5cfe1030795)。

<a id="r_a7a67f6b45a3aadc25324ef124d682375"></a>

```c
uint8_t minute
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[minute](#a18b61263b433dc5f81c2becff9c6743c)。

<a id="r_aed70238037c3c9ce06de7fd4190583ea"></a>

```c
uint8_t second
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[second](#a10b14934d80d80d3c2f0c36866bd4a64)。

<a id="r_a92aaf8cc89caae462a787d5d704a5715"></a>

```c
uint8_t valid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[valid](#a450638fda7b9d1929145575e4c576ec1)。

<a id="r_a86c5dee9be170f0bcbcad94539b9b3f9"></a>

```c
uint32_t tacc
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tacc](#a1753595f0a3935449dee4d0c57e88a6e)。

<a id="r_ae56e2991dd73ede40a6df3a4c1019267"></a>

```c
int32_t nano
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[nano](#a1c21c3b882412f36f96c59cda1d948d9)。

<a id="r_ad63cfcbcefd262731920954bab9c6758"></a>

```c
} time
```

相关声明：[time](#ad63cfcbcefd262731920954bab9c6758)。

<a id="r_a3b780d7b790b07a8ee23431969cbc318"></a>

```c
uint8_t fix_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fix_type](#a3b780d7b790b07a8ee23431969cbc318)。

<a id="r_a1bdc3cb0e4a2b6bef1c4216963e5c29c"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a1bdc3cb0e4a2b6bef1c4216963e5c29c)。

参见 `ubx_nav_fix_type`。

<a id="r_a2ff7d8bcc13ee956d9535c61efefada6"></a>

```c
uint8_t flags2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags2](#a2ff7d8bcc13ee956d9535c61efefada6)。

```c
struct {
```

<a id="r_a67d7d85b242158d926950fe83cb614a3"></a>

```c
uint8_t num_sv
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_sv](#aea613eb3d604d33120e82c569c5f10e9)。

<a id="r_aa2027a317958e0c2b6485336f93aaf91"></a>

```c
int32_t longitude
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[longitude](#ae47fc34dfd91687590bd96afe2fab091)。

<a id="r_a09c3c4cb5b9f80c46f73ee0ed7ce79a6"></a>

```c
int32_t latitude
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[latitude](#a34ec5fc41c4b323b4719803f1ff01bed)。

<a id="r_a34d4ebbb8655d2027fa3c4adcde042c0"></a>

```c
int32_t height
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[height](#ab0df156e9f8009bebfbbdb39c63c4191)。

<a id="r_a599bbd5160dc3da495e54ff53f8649d0"></a>

```c
int32_t hmsl
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[hmsl](#ae6ba97f3406b9fdbbf04c4bb3e744668)。

<a id="r_a75365db006980da777f6aa23a2eaf401"></a>

```c
uint32_t horiz_acc
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[horiz_acc](#acbb58f36eb572ce27b050a8c7540f91d)。

<a id="r_ace73b93ad4394e598bb55cbe4a84f6d9"></a>

```c
uint32_t vert_acc
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[vert_acc](#af5b3e0e70b3470bd1686ddbfefb419f9)。

<a id="r_aa47324a1a8d9dec7832aa05ed497d1bd"></a>

```c
int32_t vel_north
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[vel_north](#a1d50e696fa2684b55d04c652c85f2e16)。

<a id="r_ad1d738d44ff7dd961d9fdbef1692e947"></a>

```c
int32_t vel_east
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[vel_east](#a17c628b0acca293f068b58eff32ae4dd)。

<a id="r_ac7c655d0539df6ac16cf48851bb26694"></a>

```c
int32_t vel_down
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[vel_down](#a4958a6c11bd812477d11467ab3384161)。

<a id="r_a6231217869aff339f0415c07f2f5f11c"></a>

```c
int32_t ground_speed
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[ground_speed](#a38a8612a53966a1d598bf6d17443da7d)。

<a id="r_aee78061fdeda608f202a7bbdda0a508f"></a>

```c
int32_t head_motion
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[head_motion](#abd97f003ba43b70ffea2e9fdf5702c4f)。

<a id="r_a1e66a42bbccea1cde3b9c60152801247"></a>

```c
uint32_t speed_acc
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[speed_acc](#a955d0f7927f68f540f2e9a2c91e46e79)。

<a id="r_a6e69fc4e43e2895732fe317692a2ba97"></a>

```c
uint32_t head_acc
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[head_acc](#aa332fc93448eb6b30ad8bbaa5760db5c)。

<a id="r_a45ded7952e01728f782ca39733d19f2e"></a>

```c
uint16_t pdop
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pdop](#a7e5dc3449e52a36cb2bc5841bbf6fec8)。

航向精度估计（heading accuracy estimate），同时适用于运动航向和车辆航向。

<a id="r_a7004feb205ee0695a8b345e0e6f1fdd5"></a>

```c
uint16_t flags3
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags3](#a39b72f654fc8130c611ac839189914ed)。

<a id="r_af9762e125c820db351fcf213bb56f2d1"></a>

```c
uint32_t reserved
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved](#a80139f6d95bf943f5c6de6af1ea50e3e)。

<a id="r_a8ec172aba40e50c7e24ed61c762ed723"></a>

```c
int32_t head_vehicle
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[head_vehicle](#a8fc4b24fb8ffde02d306bc1b6770b1d8)。

<a id="r_a97a61576261674bcbc696ed467bf8c5a"></a>

```c
int16_t mag_decl
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[mag_decl](#a4f63a0f15b823e5258fdb826d2636828)。

<a id="r_a7d94889d1e20c2af10ffcb07510b8471"></a>

```c
uint16_t magacc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[magacc](#ac0265c113f01ae2bab8553eb7148e3ae)。

<a id="r_aa8b31a49c2844501505412da226872e1"></a>

```c
} nav
```

相关声明：[nav](#aa8b31a49c2844501505412da226872e1)。

## 70.2\_详细说明（Detailed Documentation）

<a id="aeadb05fe45a3a0539c899129e40059fd"></a>

### `day`

```c
uint8_t ubx_nav_pvt::day
```

<a id="a3b780d7b790b07a8ee23431969cbc318"></a>

### `fix_type`

```c
uint8_t ubx_nav_pvt::fix_type
```

<a id="a1bdc3cb0e4a2b6bef1c4216963e5c29c"></a>

### `flags`

```c
uint8_t ubx_nav_pvt::flags
```

参见 `ubx_nav_fix_type`。

<a id="a2ff7d8bcc13ee956d9535c61efefada6"></a>

### `flags2`

```c
uint8_t ubx_nav_pvt::flags2
```

<a id="a39b72f654fc8130c611ac839189914ed"></a>

### `flags3`

```c
uint16_t ubx_nav_pvt::flags3
```

<a id="a38a8612a53966a1d598bf6d17443da7d"></a>

### `ground_speed`

```c
int32_t ubx_nav_pvt::ground_speed
```

<a id="aa332fc93448eb6b30ad8bbaa5760db5c"></a>

### `head_acc`

```c
uint32_t ubx_nav_pvt::head_acc
```

<a id="abd97f003ba43b70ffea2e9fdf5702c4f"></a>

### `head_motion`

```c
int32_t ubx_nav_pvt::head_motion
```

<a id="a8fc4b24fb8ffde02d306bc1b6770b1d8"></a>

### `head_vehicle`

```c
int32_t ubx_nav_pvt::head_vehicle
```

<a id="ab0df156e9f8009bebfbbdb39c63c4191"></a>

### `height`

```c
int32_t ubx_nav_pvt::height
```

<a id="ae6ba97f3406b9fdbbf04c4bb3e744668"></a>

### `hmsl`

```c
int32_t ubx_nav_pvt::hmsl
```

<a id="acbb58f36eb572ce27b050a8c7540f91d"></a>

### `horiz_acc`

```c
uint32_t ubx_nav_pvt::horiz_acc
```

<a id="aeb710663626935d21c77a5cfe1030795"></a>

### `hour`

```c
uint8_t ubx_nav_pvt::hour
```

<a id="a426086b12ff09fb8a00dd4623fea307e"></a>

### `itow`

```c
uint32_t ubx_nav_pvt::itow
```

<a id="a34ec5fc41c4b323b4719803f1ff01bed"></a>

### `latitude`

```c
int32_t ubx_nav_pvt::latitude
```

<a id="ae47fc34dfd91687590bd96afe2fab091"></a>

### `longitude`

```c
int32_t ubx_nav_pvt::longitude
```

<a id="a4f63a0f15b823e5258fdb826d2636828"></a>

### `mag_decl`

```c
int16_t ubx_nav_pvt::mag_decl
```

<a id="ac0265c113f01ae2bab8553eb7148e3ae"></a>

### `magacc`

```c
uint16_t ubx_nav_pvt::magacc
```

<a id="a18b61263b433dc5f81c2becff9c6743c"></a>

### `minute`

```c
uint8_t ubx_nav_pvt::minute
```

<a id="ad90042dc5e00b91f004badcb0c3a5f4c"></a>

### `month`

```c
uint8_t ubx_nav_pvt::month
```

<a id="a1c21c3b882412f36f96c59cda1d948d9"></a>

### `nano`

```c
int32_t ubx_nav_pvt::nano
```

<a id="aa8b31a49c2844501505412da226872e1"></a>

### `[struct]`

```c
struct { ... } ubx_nav_pvt::nav
```

<a id="aea613eb3d604d33120e82c569c5f10e9"></a>

### `num_sv`

```c
uint8_t ubx_nav_pvt::num_sv
```

<a id="a7e5dc3449e52a36cb2bc5841bbf6fec8"></a>

### `pdop`

```c
uint16_t ubx_nav_pvt::pdop
```

航向精度估计（heading accuracy estimate），同时适用于运动航向和车辆航向。

单位为度；缩放因子为 `1e-5`。

<a id="a80139f6d95bf943f5c6de6af1ea50e3e"></a>

### `reserved`

```c
uint32_t ubx_nav_pvt::reserved
```

<a id="a10b14934d80d80d3c2f0c36866bd4a64"></a>

### `second`

```c
uint8_t ubx_nav_pvt::second
```

<a id="a955d0f7927f68f540f2e9a2c91e46e79"></a>

### `speed_acc`

```c
uint32_t ubx_nav_pvt::speed_acc
```

<a id="a1753595f0a3935449dee4d0c57e88a6e"></a>

### `tacc`

```c
uint32_t ubx_nav_pvt::tacc
```

<a id="ad63cfcbcefd262731920954bab9c6758"></a>

### `[struct]`

```c
struct { ... } ubx_nav_pvt::time
```

<a id="a450638fda7b9d1929145575e4c576ec1"></a>

### `valid`

```c
uint8_t ubx_nav_pvt::valid
```

<a id="a4958a6c11bd812477d11467ab3384161"></a>

### `vel_down`

```c
int32_t ubx_nav_pvt::vel_down
```

<a id="a17c628b0acca293f068b58eff32ae4dd"></a>

### `vel_east`

```c
int32_t ubx_nav_pvt::vel_east
```

<a id="a1d50e696fa2684b55d04c652c85f2e16"></a>

### `vel_north`

```c
int32_t ubx_nav_pvt::vel_north
```

<a id="af5b3e0e70b3470bd1686ddbfefb419f9"></a>

### `vert_acc`

```c
uint32_t ubx_nav_pvt::vert_acc
```

<a id="a84c6640806485f270b8d51d06cc49709"></a>

### `year`

```c
uint16_t ubx_nav_pvt::year
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [ubx_nav_fix_type](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h.html#a173b6c1016562da43b8131b8d8f04fef)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_ubx_mon_ver_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_ubx_nav_sat_结构体.md)
