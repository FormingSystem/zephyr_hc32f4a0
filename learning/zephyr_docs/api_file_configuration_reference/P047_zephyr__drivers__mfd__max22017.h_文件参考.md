---
id: learning.zephyr-docs.api-file-configuration-reference.page-47
title: zephyr__drivers__mfd__max22017.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/max22017_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_zephyr\_\_drivers\_\_mfd\_\_max22017.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/max22017_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 47.1\_数据结构（Data Structures）

<a id="r_max22017_5Fdata"></a>

```c
struct max22017_data
```

相关声明：[max22017_data](../device_power_control_model_reference/P023_max22017_data_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 47.2\_宏定义（Macros）

<a id="r_a69b46acb4bf6ed483c1f453a77d7c257"></a>

```c
#define MAX22017_LDAC_TOGGLE_TIME 200
```

相关声明：[MAX22017_LDAC_TOGGLE_TIME](#a69b46acb4bf6ed483c1f453a77d7c257)。

<a id="r_a6420606c34753e82d867742e2f6ff846"></a>

```c
#define MAX22017_MAX_CHANNEL 2
```

相关声明：[MAX22017_MAX_CHANNEL](#a6420606c34753e82d867742e2f6ff846)。

<a id="r_a4fb90ff0a6659973ec6f47800b04357a"></a>

```c
#define MAX22017_CRC_POLY 0x8c /* reversed 0x31 poly for crc8-maxim */
```

相关声明：[MAX22017_CRC_POLY](#a4fb90ff0a6659973ec6f47800b04357a)、[crc8](../data_utilities/P003_CRC计算接口.md#gaa614e73ee7484ca0424fa7d14a54bbb6)。

<a id="r_a29a9caa9d9f52d9d58ede62a7b09ff84"></a>

```c
#define MAX22017_GEN_ID_OFF 0x00
```

相关声明：[MAX22017_GEN_ID_OFF](#a29a9caa9d9f52d9d58ede62a7b09ff84)。

<a id="r_a395ddcfd27a1926a3787181f87242526"></a>

```c
#define MAX22017_GEN_ID_PROD_ID GENMASK(15, 8)
```

相关声明：[MAX22017_GEN_ID_PROD_ID](#a395ddcfd27a1926a3787181f87242526)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a6eb309fd6558e06a84127335e769d2d9"></a>

```c
#define MAX22017_GEN_ID_REV_ID GENMASK(7, 0)
```

相关声明：[MAX22017_GEN_ID_REV_ID](#a6eb309fd6558e06a84127335e769d2d9)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a799bc9d76c76b5cfd4e0c4782e61c68d"></a>

```c
#define MAX22017_GEN_SERIAL_MSB_OFF 0x01
```

相关声明：[MAX22017_GEN_SERIAL_MSB_OFF](#a799bc9d76c76b5cfd4e0c4782e61c68d)。

<a id="r_a71543d48878b7290f2e81ecf1689d9c5"></a>

```c
#define MAX22017_GEN_SERIAL_MSB_SERIAL_MSB GENMASK(15, 0)
```

相关声明：[MAX22017_GEN_SERIAL_MSB_SERIAL_MSB](#a71543d48878b7290f2e81ecf1689d9c5)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a269a0c9109afed5e63f29c9364d3931a"></a>

```c
#define MAX22017_GEN_SERIAL_LSB_OFF 0x02
```

相关声明：[MAX22017_GEN_SERIAL_LSB_OFF](#a269a0c9109afed5e63f29c9364d3931a)。

<a id="r_adbfda2921aaaf988e18efe7577ae8ed8"></a>

```c
#define MAX22017_GEN_SERIAL_LSB_SERIAL_LSB GENMASK(15, 0)
```

相关声明：[MAX22017_GEN_SERIAL_LSB_SERIAL_LSB](#adbfda2921aaaf988e18efe7577ae8ed8)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a8a77450cfed9423297323d451521e55d"></a>

```c
#define MAX22017_GEN_CNFG_OFF 0x03
```

相关声明：[MAX22017_GEN_CNFG_OFF](#a8a77450cfed9423297323d451521e55d)。

<a id="r_a77447c3bae3e076fe6c19eb761e54d0a"></a>

```c
#define MAX22017_GEN_CNFG_OPENWIRE_DTCT_CNFG GENMASK(15, 14)
```

相关声明：[MAX22017_GEN_CNFG_OPENWIRE_DTCT_CNFG](#a77447c3bae3e076fe6c19eb761e54d0a)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_aa3c6c039ffd5caeb411e8f057351a47b"></a>

```c
#define MAX22017_GEN_CNFG_TMOUT_SEL GENMASK(13, 10)
```

相关声明：[MAX22017_GEN_CNFG_TMOUT_SEL](#aa3c6c039ffd5caeb411e8f057351a47b)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a888207719162d5eb973e65f8f16bcee9"></a>

```c
#define MAX22017_GEN_CNFG_TMOUT_CNFG BIT(9)
```

相关声明：[MAX22017_GEN_CNFG_TMOUT_CNFG](#a888207719162d5eb973e65f8f16bcee9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a3d90df4835aa9814d64ed157ba55dc89"></a>

```c
#define MAX22017_GEN_CNFG_TMOUT_EN BIT(8)
```

相关声明：[MAX22017_GEN_CNFG_TMOUT_EN](#a3d90df4835aa9814d64ed157ba55dc89)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a53ff3e5d22a4121c5a8e0d468f62adfe"></a>

```c
#define MAX22017_GEN_CNFG_THSHDN_CNFG GENMASK(7, 6)
```

相关声明：[MAX22017_GEN_CNFG_THSHDN_CNFG](#a53ff3e5d22a4121c5a8e0d468f62adfe)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ab8ee545a7f918e680496c733bc094d1b"></a>

```c
#define MAX22017_GEN_CNFG_OVC_SHDN_CNFG GENMASK(5, 4)
```

相关声明：[MAX22017_GEN_CNFG_OVC_SHDN_CNFG](#ab8ee545a7f918e680496c733bc094d1b)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_aad7bdcad31409154f76037090a602f2d"></a>

```c
#define MAX22017_GEN_CNFG_OVC_CNFG GENMASK(3, 2)
```

相关声明：[MAX22017_GEN_CNFG_OVC_CNFG](#aad7bdcad31409154f76037090a602f2d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ad677c0bfb0565436848ce8fa3ab497b1"></a>

```c
#define MAX22017_GEN_CNFG_CRC_EN BIT(1)
```

相关声明：[MAX22017_GEN_CNFG_CRC_EN](#ad677c0bfb0565436848ce8fa3ab497b1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a2ef6bf6ae5c000d84f5910f6ba5c55ba"></a>

```c
#define MAX22017_GEN_CNFG_DACREF_SEL BIT(0)
```

相关声明：[MAX22017_GEN_CNFG_DACREF_SEL](#a2ef6bf6ae5c000d84f5910f6ba5c55ba)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a9197693c7b15a5337a19659efc2e250c"></a>

```c
#define MAX22017_GEN_GPIO_CTRL_OFF 0x04
```

相关声明：[MAX22017_GEN_GPIO_CTRL_OFF](#a9197693c7b15a5337a19659efc2e250c)。

<a id="r_abe8bd23109b597ea8349316c0d1d8427"></a>

```c
#define MAX22017_GEN_GPIO_CTRL_GPIO_EN GENMASK(13, 8)
```

相关声明：[MAX22017_GEN_GPIO_CTRL_GPIO_EN](#abe8bd23109b597ea8349316c0d1d8427)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a52d221379e6bcdba5ed8d2f287b64f84"></a>

```c
#define MAX22017_GEN_GPIO_CTRL_GPIO_DIR GENMASK(5, 0)
```

相关声明：[MAX22017_GEN_GPIO_CTRL_GPIO_DIR](#a52d221379e6bcdba5ed8d2f287b64f84)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_adac6b2dde0ca575d402e781f4ecf5420"></a>

```c
#define MAX22017_GEN_GPIO_DATA_OFF 0x05
```

相关声明：[MAX22017_GEN_GPIO_DATA_OFF](#adac6b2dde0ca575d402e781f4ecf5420)。

<a id="r_a0c2800b8921081669472db86ce0c92d3"></a>

```c
#define MAX22017_GEN_GPIO_DATA_GPO_DATA GENMASK(13, 8)
```

相关声明：[MAX22017_GEN_GPIO_DATA_GPO_DATA](#a0c2800b8921081669472db86ce0c92d3)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a43846e179219f0738c1ad1a4b464ab32"></a>

```c
#define MAX22017_GEN_GPIO_DATA_GPI_DATA GENMASK(5, 0)
```

相关声明：[MAX22017_GEN_GPIO_DATA_GPI_DATA](#a43846e179219f0738c1ad1a4b464ab32)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ab46c131ba1e50d5f86c3e27b807b7a7b"></a>

```c
#define MAX22017_GEN_GPI_INT_OFF 0x06
```

相关声明：[MAX22017_GEN_GPI_INT_OFF](#ab46c131ba1e50d5f86c3e27b807b7a7b)。

<a id="r_acb8737f0e19a94dc66024cda4536208f"></a>

```c
#define MAX22017_GEN_GPI_INT_GPI_POS_EDGE_INT GENMASK(13, 8)
```

相关声明：[MAX22017_GEN_GPI_INT_GPI_POS_EDGE_INT](#acb8737f0e19a94dc66024cda4536208f)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_abc8ca54142d80a1d14a63092e553b582"></a>

```c
#define MAX22017_GEN_GPI_INT_GPI_NEG_EDGE_INT GENMASK(5, 0)
```

相关声明：[MAX22017_GEN_GPI_INT_GPI_NEG_EDGE_INT](#abc8ca54142d80a1d14a63092e553b582)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a24277b36f8fe9b994fa8de1c63c06fed"></a>

```c
#define MAX22017_GEN_GPI_INT_STA_OFF 0x07
```

相关声明：[MAX22017_GEN_GPI_INT_STA_OFF](#a24277b36f8fe9b994fa8de1c63c06fed)。

<a id="r_ab3f2d018f43cda0121afed3f920d631f"></a>

```c
#define MAX22017_GEN_GPI_INT_STA_GPI_POS_EDGE_INT_STA GENMASK(13, 8)
```

相关声明：[MAX22017_GEN_GPI_INT_STA_GPI_POS_EDGE_INT_STA](#ab3f2d018f43cda0121afed3f920d631f)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a2428e64221646898a7fc8dc68e350f5e"></a>

```c
#define MAX22017_GEN_GPI_INT_STA_GPI_NEG_EDGE_INT_STA GENMASK(5, 0)
```

相关声明：[MAX22017_GEN_GPI_INT_STA_GPI_NEG_EDGE_INT_STA](#a2428e64221646898a7fc8dc68e350f5e)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_aad01e617a20eed924aa47003d7a73ef4"></a>

```c
#define MAX22017_GEN_INT_OFF 0x08
```

相关声明：[MAX22017_GEN_INT_OFF](#aad01e617a20eed924aa47003d7a73ef4)。

<a id="r_a950db8f0491cb67a25eb2eb5ad740a70"></a>

```c
#define MAX22017_GEN_INT_FAIL_INT BIT(15)
```

相关声明：[MAX22017_GEN_INT_FAIL_INT](#a950db8f0491cb67a25eb2eb5ad740a70)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a27eac9949479c8d1f42f68da05d39383"></a>

```c
#define MAX22017_GEN_INT_CONV_OVF_INT GENMASK(13, 12)
```

相关声明：[MAX22017_GEN_INT_CONV_OVF_INT](#a27eac9949479c8d1f42f68da05d39383)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ae956e4148f8da78321a8b444495da665"></a>

```c
#define MAX22017_GEN_INT_OPENWIRE_DTCT_INT GENMASK(11, 10)
```

相关声明：[MAX22017_GEN_INT_OPENWIRE_DTCT_INT](#ae956e4148f8da78321a8b444495da665)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ac9bf908c94cb4d7949f74d288b8cafeb"></a>

```c
#define MAX22017_GEN_INT_HVDD_INT BIT(9)
```

相关声明：[MAX22017_GEN_INT_HVDD_INT](#ac9bf908c94cb4d7949f74d288b8cafeb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab0dae9b77818a8fee73d5b997cdc9a3c"></a>

```c
#define MAX22017_GEN_INT_TMOUT_INT BIT(8)
```

相关声明：[MAX22017_GEN_INT_TMOUT_INT](#ab0dae9b77818a8fee73d5b997cdc9a3c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a7833344d8d071ba5d591391294e3392f"></a>

```c
#define MAX22017_GEN_INT_THSHDN_INT GENMASK(7, 6)
```

相关声明：[MAX22017_GEN_INT_THSHDN_INT](#a7833344d8d071ba5d591391294e3392f)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a22d2450dd425193fb6a68e4b337fb05d"></a>

```c
#define MAX22017_GEN_INT_THWRNG_INT GENMASK(5, 4)
```

相关声明：[MAX22017_GEN_INT_THWRNG_INT](#a22d2450dd425193fb6a68e4b337fb05d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a950ee60a66d4770719dc285ec8233ba8"></a>

```c
#define MAX22017_GEN_INT_OVC_INT GENMASK(3, 2)
```

相关声明：[MAX22017_GEN_INT_OVC_INT](#a950ee60a66d4770719dc285ec8233ba8)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ac5582d36610f0eb5b0795d6c20c6dfce"></a>

```c
#define MAX22017_GEN_INT_CRC_INT BIT(1)
```

相关声明：[MAX22017_GEN_INT_CRC_INT](#ac5582d36610f0eb5b0795d6c20c6dfce)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad9a98581421dd420920ca8b499131594"></a>

```c
#define MAX22017_GEN_INT_GPI_INT BIT(0)
```

相关声明：[MAX22017_GEN_INT_GPI_INT](#ad9a98581421dd420920ca8b499131594)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_afaa5cf0a23d3b86bdb0aa8f64794a349"></a>

```c
#define MAX22017_GEN_INTEN_OFF 0x09
```

相关声明：[MAX22017_GEN_INTEN_OFF](#afaa5cf0a23d3b86bdb0aa8f64794a349)。

<a id="r_a569d0198591bd1ac8cf3017985797161"></a>

```c
#define MAX22017_GEN_INTEN_CONV_OVF_INTEN GENMASK(13, 12)
```

相关声明：[MAX22017_GEN_INTEN_CONV_OVF_INTEN](#a569d0198591bd1ac8cf3017985797161)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ab0d04e5d3b9a275e2f6d358d55f9ecec"></a>

```c
#define MAX22017_GEN_INTEN_OPENWIRE_DTCT_INTEN GENMASK(11, 10)
```

相关声明：[MAX22017_GEN_INTEN_OPENWIRE_DTCT_INTEN](#ab0d04e5d3b9a275e2f6d358d55f9ecec)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a27665ac4ca4283876c7b0d82c68a0955"></a>

```c
#define MAX22017_GEN_INTEN_HVDD_INTEN BIT(9)
```

相关声明：[MAX22017_GEN_INTEN_HVDD_INTEN](#a27665ac4ca4283876c7b0d82c68a0955)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a3759acb5df5704f36d97c159561efd10"></a>

```c
#define MAX22017_GEN_INTEN_TMOUT_INTEN BIT(8)
```

相关声明：[MAX22017_GEN_INTEN_TMOUT_INTEN](#a3759acb5df5704f36d97c159561efd10)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a53365f203a2a2d4687807a7e709edfe7"></a>

```c
#define MAX22017_GEN_INTEN_THSHDN_INTEN GENMASK(7, 6)
```

相关声明：[MAX22017_GEN_INTEN_THSHDN_INTEN](#a53365f203a2a2d4687807a7e709edfe7)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a9e9534a6244dc77b41b464be99997306"></a>

```c
#define MAX22017_GEN_INTEN_THWRNG_INTEN GENMASK(5, 4)
```

相关声明：[MAX22017_GEN_INTEN_THWRNG_INTEN](#a9e9534a6244dc77b41b464be99997306)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a9ec0c3a38830359ca2eebecc37275fe5"></a>

```c
#define MAX22017_GEN_INTEN_OVC_INTEN GENMASK(3, 2)
```

相关声明：[MAX22017_GEN_INTEN_OVC_INTEN](#a9ec0c3a38830359ca2eebecc37275fe5)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_aabcebfeedc9571ed8d951bf876fe4231"></a>

```c
#define MAX22017_GEN_INTEN_CRC_INTEN BIT(1)
```

相关声明：[MAX22017_GEN_INTEN_CRC_INTEN](#aabcebfeedc9571ed8d951bf876fe4231)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0ae1361d7e475c8a4eb2850d132a4498"></a>

```c
#define MAX22017_GEN_INTEN_GPI_INTEN BIT(0)
```

相关声明：[MAX22017_GEN_INTEN_GPI_INTEN](#a0ae1361d7e475c8a4eb2850d132a4498)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a291a4ec441b4374377950c4c7f4badbf"></a>

```c
#define MAX22017_GEN_RST_CTRL_OFF 0x0A
```

相关声明：[MAX22017_GEN_RST_CTRL_OFF](#a291a4ec441b4374377950c4c7f4badbf)。

<a id="r_a1693f93cd62731fe95c7ce1e1007d800"></a>

```c
#define MAX22017_GEN_RST_CTRL_AO_COEFF_RELOAD GENMASK(15, 14)
```

相关声明：[MAX22017_GEN_RST_CTRL_AO_COEFF_RELOAD](#a1693f93cd62731fe95c7ce1e1007d800)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ad544ab22f6ebf4a5a0d794a92145e2b5"></a>

```c
#define MAX22017_GEN_RST_CTRL_GEN_RST BIT(9)
```

相关声明：[MAX22017_GEN_RST_CTRL_GEN_RST](#ad544ab22f6ebf4a5a0d794a92145e2b5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a3bcd3cbd0b9e3fb93e24388a0b384ae9"></a>

```c
#define MAX22017_AO_CMD_OFF 0x40
```

相关声明：[MAX22017_AO_CMD_OFF](#a3bcd3cbd0b9e3fb93e24388a0b384ae9)。

<a id="r_a4e77f6704c235280628933321f691712"></a>

```c
#define MAX22017_AO_CMD_AO_LD_CTRL GENMASK(15, 14)
```

相关声明：[MAX22017_AO_CMD_AO_LD_CTRL](#a4e77f6704c235280628933321f691712)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a9ed535b03f0aede89e5309005cec296c"></a>

```c
#define MAX22017_AO_STA_OFF 0x41
```

相关声明：[MAX22017_AO_STA_OFF](#a9ed535b03f0aede89e5309005cec296c)。

<a id="r_a3b4266da3e1fd880341e3bf3c4789ad1"></a>

```c
#define MAX22017_AO_STA_BUSY_STA GENMASK(15, 14)
```

相关声明：[MAX22017_AO_STA_BUSY_STA](#a3b4266da3e1fd880341e3bf3c4789ad1)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ab483e9896b6884a238d560d5e2f988cc"></a>

```c
#define MAX22017_AO_STA_SLEW_STA GENMASK(13, 12)
```

相关声明：[MAX22017_AO_STA_SLEW_STA](#ab483e9896b6884a238d560d5e2f988cc)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_afef14d877f9cb5771f70ed20ef2b6619"></a>

```c
#define MAX22017_AO_STA_FAIL_STA BIT(0)
```

相关声明：[MAX22017_AO_STA_FAIL_STA](#afef14d877f9cb5771f70ed20ef2b6619)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a2bd588d5437464244088f003b9c2665f"></a>

```c
#define MAX22017_AO_CNFG_OFF 0x42
```

相关声明：[MAX22017_AO_CNFG_OFF](#a2bd588d5437464244088f003b9c2665f)。

<a id="r_af1add45a9664316f60a653369562fa9c"></a>

```c
#define MAX22017_AO_CNFG_AO_LD_CNFG GENMASK(15, 14)
```

相关声明：[MAX22017_AO_CNFG_AO_LD_CNFG](#af1add45a9664316f60a653369562fa9c)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a018306445ab0bd9305f7e9ca311936bc"></a>

```c
#define MAX22017_AO_CNFG_AO_CM_SENSE GENMASK(13, 12)
```

相关声明：[MAX22017_AO_CNFG_AO_CM_SENSE](#a018306445ab0bd9305f7e9ca311936bc)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a39a986f264a8f861f91b8e139e8085de"></a>

```c
#define MAX22017_AO_CNFG_AO_UNI GENMASK(11, 10)
```

相关声明：[MAX22017_AO_CNFG_AO_UNI](#a39a986f264a8f861f91b8e139e8085de)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a5293ea7da75751e93c0130c306727bda"></a>

```c
#define MAX22017_AO_CNFG_AO_MODE GENMASK(9, 8)
```

相关声明：[MAX22017_AO_CNFG_AO_MODE](#a5293ea7da75751e93c0130c306727bda)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_aadf01e360a09401fdcaef4fc4ec39265"></a>

```c
#define MAX22017_AO_CNFG_AO_OPENWIRE_DTCT_LMT GENMASK(5, 4)
```

相关声明：[MAX22017_AO_CNFG_AO_OPENWIRE_DTCT_LMT](#aadf01e360a09401fdcaef4fc4ec39265)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a5d44e9a362380c61176052e98afadaf5"></a>

```c
#define MAX22017_AO_CNFG_AI_EN GENMASK(3, 2)
```

相关声明：[MAX22017_AO_CNFG_AI_EN](#a5d44e9a362380c61176052e98afadaf5)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ab2dfe72b9fa038e192c7daae2ffb3bd5"></a>

```c
#define MAX22017_AO_CNFG_AO_EN GENMASK(1, 0)
```

相关声明：[MAX22017_AO_CNFG_AO_EN](#ab2dfe72b9fa038e192c7daae2ffb3bd5)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a30e655032be25236b337941649ab4587"></a>

```c
#define MAX22017_AO_SLEW_RATE_CHn_OFF(n)
```

相关声明：[MAX22017_AO_SLEW_RATE_CHn_OFF](#a30e655032be25236b337941649ab4587)。

<a id="r_aead931e808873a41e7749083abdb5bc9"></a>

```c
#define MAX22017_AO_SLEW_RATE_CHn_AO_SR_EN_CHn BIT(5)
```

相关声明：[MAX22017_AO_SLEW_RATE_CHn_AO_SR_EN_CHn](#aead931e808873a41e7749083abdb5bc9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5e59cb1143c01be37e3cbf7cb8db35eb"></a>

```c
#define MAX22017_AO_SLEW_RATE_CHn_AO_SR_SEL_CHn BIT(4)
```

相关声明：[MAX22017_AO_SLEW_RATE_CHn_AO_SR_SEL_CHn](#a5e59cb1143c01be37e3cbf7cb8db35eb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a882b209cbcb535cb10102a2f21501482"></a>

```c
#define MAX22017_AO_SLEW_RATE_CHn_AO_SR_STEP_SIZE_CHn GENMASK(3, 2)
```

相关声明：[MAX22017_AO_SLEW_RATE_CHn_AO_SR_STEP_SIZE_CHn](#a882b209cbcb535cb10102a2f21501482)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a59f3f06a4a2405bbc96df4b487b35cd4"></a>

```c
#define MAX22017_AO_SLEW_RATE_CHn_AO_SR_UPDATE_RATE_CHn GENMASK(1, 0)
```

相关声明：[MAX22017_AO_SLEW_RATE_CHn_AO_SR_UPDATE_RATE_CHn](#a59f3f06a4a2405bbc96df4b487b35cd4)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a7bcc6214915085619e5f549557d78ea4"></a>

```c
#define MAX22017_AO_DATA_CHn_OFF(n)
```

相关声明：[MAX22017_AO_DATA_CHn_OFF](#a7bcc6214915085619e5f549557d78ea4)。

<a id="r_a37a9fc76107c849f89d1db6914db1ab9"></a>

```c
#define MAX22017_AO_DATA_CHn_AO_DATA_CH GENMASK(15, 0)
```

相关声明：[MAX22017_AO_DATA_CHn_AO_DATA_CH](#a37a9fc76107c849f89d1db6914db1ab9)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ab31ff3c83a67336f3c62e8ca08f3dd25"></a>

```c
#define MAX22017_AO_OFFSET_CORR_CHn_OFF(n)
```

相关声明：[MAX22017_AO_OFFSET_CORR_CHn_OFF](#ab31ff3c83a67336f3c62e8ca08f3dd25)。

<a id="r_a4ed090f64827549887dec94b9c159f3b"></a>

```c
#define MAX22017_AO_OFFSET_CORR_CHn_AO_OFFSET_CH GENMASK(15, 0)
```

相关声明：[MAX22017_AO_OFFSET_CORR_CHn_AO_OFFSET_CH](#a4ed090f64827549887dec94b9c159f3b)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a5e40e0dffc60182fe012069d31d6b881"></a>

```c
#define MAX22017_AO_GAIN_CORR_CHn_OFF(n)
```

相关声明：[MAX22017_AO_GAIN_CORR_CHn_OFF](#a5e40e0dffc60182fe012069d31d6b881)。

<a id="r_afb46c37c05d65b550178a22c7fa388aa"></a>

```c
#define MAX22017_AO_GAIN_CORR_CHn_AO_GAIN_CH GENMASK(15, 0)
```

相关声明：[MAX22017_AO_GAIN_CORR_CHn_AO_GAIN_CH](#afb46c37c05d65b550178a22c7fa388aa)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_aa1b178c2a60337d8b9dcfb4ac8315d14"></a>

```c
#define MAX22017_SPI_TRANS_ADDR GENMASK(7, 1)
```

相关声明：[MAX22017_SPI_TRANS_ADDR](#aa1b178c2a60337d8b9dcfb4ac8315d14)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a0189fe593af9379781b6f63998b2d268"></a>

```c
#define MAX22017_SPI_TRANS_DIR BIT(0)
```

相关声明：[MAX22017_SPI_TRANS_DIR](#a0189fe593af9379781b6f63998b2d268)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa16b8b5dc1817df754d5228f4c335fc9"></a>

```c
#define MAX22017_SPI_TRANS_PAYLOAD GENMASK(15, 0)
```

相关声明：[MAX22017_SPI_TRANS_PAYLOAD](#aa16b8b5dc1817df754d5228f4c335fc9)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 47.3\_函数（Functions）

<a id="r_ga7c051fa0697ae672a4dddbfa84059ad0"></a>

```c
int max22017_reg_read (const struct device *dev, uint8_t addr, uint16_t *value)
```

相关声明：[max22017_reg_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__max22017.html#ga7c051fa0697ae672a4dddbfa84059ad0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 max22017 的寄存器（Register）。

<a id="r_gac4a4a29f7ae31af97f19d700264a604d"></a>

```c
int max22017_reg_write (const struct device *dev, uint8_t addr, uint16_t value)
```

相关声明：[max22017_reg_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__max22017.html#gac4a4a29f7ae31af97f19d700264a604d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

写入 max22017 的寄存器（Register）。

## 47.4\_详细说明（Detailed Documentation）

<a id="a4e77f6704c235280628933321f691712"></a>

### `MAX22017_AO_CMD_AO_LD_CTRL`

```c
#define MAX22017_AO_CMD_AO_LD_CTRL GENMASK(15, 14)
```

<a id="a3bcd3cbd0b9e3fb93e24388a0b384ae9"></a>

### `MAX22017_AO_CMD_OFF`

```c
#define MAX22017_AO_CMD_OFF 0x40
```

<a id="a5d44e9a362380c61176052e98afadaf5"></a>

### `MAX22017_AO_CNFG_AI_EN`

```c
#define MAX22017_AO_CNFG_AI_EN GENMASK(3, 2)
```

<a id="a018306445ab0bd9305f7e9ca311936bc"></a>

### `MAX22017_AO_CNFG_AO_CM_SENSE`

```c
#define MAX22017_AO_CNFG_AO_CM_SENSE GENMASK(13, 12)
```

<a id="ab2dfe72b9fa038e192c7daae2ffb3bd5"></a>

### `MAX22017_AO_CNFG_AO_EN`

```c
#define MAX22017_AO_CNFG_AO_EN GENMASK(1, 0)
```

<a id="af1add45a9664316f60a653369562fa9c"></a>

### `MAX22017_AO_CNFG_AO_LD_CNFG`

```c
#define MAX22017_AO_CNFG_AO_LD_CNFG GENMASK(15, 14)
```

<a id="a5293ea7da75751e93c0130c306727bda"></a>

### `MAX22017_AO_CNFG_AO_MODE`

```c
#define MAX22017_AO_CNFG_AO_MODE GENMASK(9, 8)
```

<a id="aadf01e360a09401fdcaef4fc4ec39265"></a>

### `MAX22017_AO_CNFG_AO_OPENWIRE_DTCT_LMT`

```c
#define MAX22017_AO_CNFG_AO_OPENWIRE_DTCT_LMT GENMASK(5, 4)
```

<a id="a39a986f264a8f861f91b8e139e8085de"></a>

### `MAX22017_AO_CNFG_AO_UNI`

```c
#define MAX22017_AO_CNFG_AO_UNI GENMASK(11, 10)
```

<a id="a2bd588d5437464244088f003b9c2665f"></a>

### `MAX22017_AO_CNFG_OFF`

```c
#define MAX22017_AO_CNFG_OFF 0x42
```

<a id="a37a9fc76107c849f89d1db6914db1ab9"></a>

### `MAX22017_AO_DATA_CHn_AO_DATA_CH`

```c
#define MAX22017_AO_DATA_CHn_AO_DATA_CH GENMASK(15, 0)
```

<a id="a7bcc6214915085619e5f549557d78ea4"></a>

### `MAX22017_AO_DATA_CHn_OFF`

```c
#define MAX22017_AO_DATA_CHn_OFF ( n)
```

展开值（Value）：

```c
(0x45 + n)
```

<a id="afb46c37c05d65b550178a22c7fa388aa"></a>

### `MAX22017_AO_GAIN_CORR_CHn_AO_GAIN_CH`

```c
#define MAX22017_AO_GAIN_CORR_CHn_AO_GAIN_CH GENMASK(15, 0)
```

<a id="a5e40e0dffc60182fe012069d31d6b881"></a>

### `MAX22017_AO_GAIN_CORR_CHn_OFF`

```c
#define MAX22017_AO_GAIN_CORR_CHn_OFF ( n)
```

展开值（Value）：

```c
(0x48 + (2 * n))
```

<a id="a4ed090f64827549887dec94b9c159f3b"></a>

### `MAX22017_AO_OFFSET_CORR_CHn_AO_OFFSET_CH`

```c
#define MAX22017_AO_OFFSET_CORR_CHn_AO_OFFSET_CH GENMASK(15, 0)
```

<a id="ab31ff3c83a67336f3c62e8ca08f3dd25"></a>

### `MAX22017_AO_OFFSET_CORR_CHn_OFF`

```c
#define MAX22017_AO_OFFSET_CORR_CHn_OFF ( n)
```

展开值（Value）：

```c
(0x47 + (2 * n))
```

<a id="aead931e808873a41e7749083abdb5bc9"></a>

### `MAX22017_AO_SLEW_RATE_CHn_AO_SR_EN_CHn`

```c
#define MAX22017_AO_SLEW_RATE_CHn_AO_SR_EN_CHn BIT(5)
```

<a id="a5e59cb1143c01be37e3cbf7cb8db35eb"></a>

### `MAX22017_AO_SLEW_RATE_CHn_AO_SR_SEL_CHn`

```c
#define MAX22017_AO_SLEW_RATE_CHn_AO_SR_SEL_CHn BIT(4)
```

<a id="a882b209cbcb535cb10102a2f21501482"></a>

### `MAX22017_AO_SLEW_RATE_CHn_AO_SR_STEP_SIZE_CHn`

```c
#define MAX22017_AO_SLEW_RATE_CHn_AO_SR_STEP_SIZE_CHn GENMASK(3, 2)
```

<a id="a59f3f06a4a2405bbc96df4b487b35cd4"></a>

### `MAX22017_AO_SLEW_RATE_CHn_AO_SR_UPDATE_RATE_CHn`

```c
#define MAX22017_AO_SLEW_RATE_CHn_AO_SR_UPDATE_RATE_CHn GENMASK(1, 0)
```

<a id="a30e655032be25236b337941649ab4587"></a>

### `MAX22017_AO_SLEW_RATE_CHn_OFF`

```c
#define MAX22017_AO_SLEW_RATE_CHn_OFF ( n)
```

展开值（Value）：

```c
(0x43 + n)
```

<a id="a3b4266da3e1fd880341e3bf3c4789ad1"></a>

### `MAX22017_AO_STA_BUSY_STA`

```c
#define MAX22017_AO_STA_BUSY_STA GENMASK(15, 14)
```

<a id="afef14d877f9cb5771f70ed20ef2b6619"></a>

### `MAX22017_AO_STA_FAIL_STA`

```c
#define MAX22017_AO_STA_FAIL_STA BIT(0)
```

<a id="a9ed535b03f0aede89e5309005cec296c"></a>

### `MAX22017_AO_STA_OFF`

```c
#define MAX22017_AO_STA_OFF 0x41
```

<a id="ab483e9896b6884a238d560d5e2f988cc"></a>

### `MAX22017_AO_STA_SLEW_STA`

```c
#define MAX22017_AO_STA_SLEW_STA GENMASK(13, 12)
```

<a id="a4fb90ff0a6659973ec6f47800b04357a"></a>

### `MAX22017_CRC_POLY`

```c
#define MAX22017_CRC_POLY 0x8c /* reversed 0x31 poly for crc8-maxim */
```

<a id="ad677c0bfb0565436848ce8fa3ab497b1"></a>

### `MAX22017_GEN_CNFG_CRC_EN`

```c
#define MAX22017_GEN_CNFG_CRC_EN BIT(1)
```

<a id="a2ef6bf6ae5c000d84f5910f6ba5c55ba"></a>

### `MAX22017_GEN_CNFG_DACREF_SEL`

```c
#define MAX22017_GEN_CNFG_DACREF_SEL BIT(0)
```

<a id="a8a77450cfed9423297323d451521e55d"></a>

### `MAX22017_GEN_CNFG_OFF`

```c
#define MAX22017_GEN_CNFG_OFF 0x03
```

<a id="a77447c3bae3e076fe6c19eb761e54d0a"></a>

### `MAX22017_GEN_CNFG_OPENWIRE_DTCT_CNFG`

```c
#define MAX22017_GEN_CNFG_OPENWIRE_DTCT_CNFG GENMASK(15, 14)
```

<a id="aad7bdcad31409154f76037090a602f2d"></a>

### `MAX22017_GEN_CNFG_OVC_CNFG`

```c
#define MAX22017_GEN_CNFG_OVC_CNFG GENMASK(3, 2)
```

<a id="ab8ee545a7f918e680496c733bc094d1b"></a>

### `MAX22017_GEN_CNFG_OVC_SHDN_CNFG`

```c
#define MAX22017_GEN_CNFG_OVC_SHDN_CNFG GENMASK(5, 4)
```

<a id="a53ff3e5d22a4121c5a8e0d468f62adfe"></a>

### `MAX22017_GEN_CNFG_THSHDN_CNFG`

```c
#define MAX22017_GEN_CNFG_THSHDN_CNFG GENMASK(7, 6)
```

<a id="a888207719162d5eb973e65f8f16bcee9"></a>

### `MAX22017_GEN_CNFG_TMOUT_CNFG`

```c
#define MAX22017_GEN_CNFG_TMOUT_CNFG BIT(9)
```

<a id="a3d90df4835aa9814d64ed157ba55dc89"></a>

### `MAX22017_GEN_CNFG_TMOUT_EN`

```c
#define MAX22017_GEN_CNFG_TMOUT_EN BIT(8)
```

<a id="aa3c6c039ffd5caeb411e8f057351a47b"></a>

### `MAX22017_GEN_CNFG_TMOUT_SEL`

```c
#define MAX22017_GEN_CNFG_TMOUT_SEL GENMASK(13, 10)
```

<a id="abc8ca54142d80a1d14a63092e553b582"></a>

### `MAX22017_GEN_GPI_INT_GPI_NEG_EDGE_INT`

```c
#define MAX22017_GEN_GPI_INT_GPI_NEG_EDGE_INT GENMASK(5, 0)
```

<a id="acb8737f0e19a94dc66024cda4536208f"></a>

### `MAX22017_GEN_GPI_INT_GPI_POS_EDGE_INT`

```c
#define MAX22017_GEN_GPI_INT_GPI_POS_EDGE_INT GENMASK(13, 8)
```

<a id="ab46c131ba1e50d5f86c3e27b807b7a7b"></a>

### `MAX22017_GEN_GPI_INT_OFF`

```c
#define MAX22017_GEN_GPI_INT_OFF 0x06
```

<a id="a2428e64221646898a7fc8dc68e350f5e"></a>

### `MAX22017_GEN_GPI_INT_STA_GPI_NEG_EDGE_INT_STA`

```c
#define MAX22017_GEN_GPI_INT_STA_GPI_NEG_EDGE_INT_STA GENMASK(5, 0)
```

<a id="ab3f2d018f43cda0121afed3f920d631f"></a>

### `MAX22017_GEN_GPI_INT_STA_GPI_POS_EDGE_INT_STA`

```c
#define MAX22017_GEN_GPI_INT_STA_GPI_POS_EDGE_INT_STA GENMASK(13, 8)
```

<a id="a24277b36f8fe9b994fa8de1c63c06fed"></a>

### `MAX22017_GEN_GPI_INT_STA_OFF`

```c
#define MAX22017_GEN_GPI_INT_STA_OFF 0x07
```

<a id="a52d221379e6bcdba5ed8d2f287b64f84"></a>

### `MAX22017_GEN_GPIO_CTRL_GPIO_DIR`

```c
#define MAX22017_GEN_GPIO_CTRL_GPIO_DIR GENMASK(5, 0)
```

<a id="abe8bd23109b597ea8349316c0d1d8427"></a>

### `MAX22017_GEN_GPIO_CTRL_GPIO_EN`

```c
#define MAX22017_GEN_GPIO_CTRL_GPIO_EN GENMASK(13, 8)
```

<a id="a9197693c7b15a5337a19659efc2e250c"></a>

### `MAX22017_GEN_GPIO_CTRL_OFF`

```c
#define MAX22017_GEN_GPIO_CTRL_OFF 0x04
```

<a id="a43846e179219f0738c1ad1a4b464ab32"></a>

### `MAX22017_GEN_GPIO_DATA_GPI_DATA`

```c
#define MAX22017_GEN_GPIO_DATA_GPI_DATA GENMASK(5, 0)
```

<a id="a0c2800b8921081669472db86ce0c92d3"></a>

### `MAX22017_GEN_GPIO_DATA_GPO_DATA`

```c
#define MAX22017_GEN_GPIO_DATA_GPO_DATA GENMASK(13, 8)
```

<a id="adac6b2dde0ca575d402e781f4ecf5420"></a>

### `MAX22017_GEN_GPIO_DATA_OFF`

```c
#define MAX22017_GEN_GPIO_DATA_OFF 0x05
```

<a id="a29a9caa9d9f52d9d58ede62a7b09ff84"></a>

### `MAX22017_GEN_ID_OFF`

```c
#define MAX22017_GEN_ID_OFF 0x00
```

<a id="a395ddcfd27a1926a3787181f87242526"></a>

### `MAX22017_GEN_ID_PROD_ID`

```c
#define MAX22017_GEN_ID_PROD_ID GENMASK(15, 8)
```

<a id="a6eb309fd6558e06a84127335e769d2d9"></a>

### `MAX22017_GEN_ID_REV_ID`

```c
#define MAX22017_GEN_ID_REV_ID GENMASK(7, 0)
```

<a id="a27eac9949479c8d1f42f68da05d39383"></a>

### `MAX22017_GEN_INT_CONV_OVF_INT`

```c
#define MAX22017_GEN_INT_CONV_OVF_INT GENMASK(13, 12)
```

<a id="ac5582d36610f0eb5b0795d6c20c6dfce"></a>

### `MAX22017_GEN_INT_CRC_INT`

```c
#define MAX22017_GEN_INT_CRC_INT BIT(1)
```

<a id="a950db8f0491cb67a25eb2eb5ad740a70"></a>

### `MAX22017_GEN_INT_FAIL_INT`

```c
#define MAX22017_GEN_INT_FAIL_INT BIT(15)
```

<a id="ad9a98581421dd420920ca8b499131594"></a>

### `MAX22017_GEN_INT_GPI_INT`

```c
#define MAX22017_GEN_INT_GPI_INT BIT(0)
```

<a id="ac9bf908c94cb4d7949f74d288b8cafeb"></a>

### `MAX22017_GEN_INT_HVDD_INT`

```c
#define MAX22017_GEN_INT_HVDD_INT BIT(9)
```

<a id="aad01e617a20eed924aa47003d7a73ef4"></a>

### `MAX22017_GEN_INT_OFF`

```c
#define MAX22017_GEN_INT_OFF 0x08
```

<a id="ae956e4148f8da78321a8b444495da665"></a>

### `MAX22017_GEN_INT_OPENWIRE_DTCT_INT`

```c
#define MAX22017_GEN_INT_OPENWIRE_DTCT_INT GENMASK(11, 10)
```

<a id="a950ee60a66d4770719dc285ec8233ba8"></a>

### `MAX22017_GEN_INT_OVC_INT`

```c
#define MAX22017_GEN_INT_OVC_INT GENMASK(3, 2)
```

<a id="a7833344d8d071ba5d591391294e3392f"></a>

### `MAX22017_GEN_INT_THSHDN_INT`

```c
#define MAX22017_GEN_INT_THSHDN_INT GENMASK(7, 6)
```

<a id="a22d2450dd425193fb6a68e4b337fb05d"></a>

### `MAX22017_GEN_INT_THWRNG_INT`

```c
#define MAX22017_GEN_INT_THWRNG_INT GENMASK(5, 4)
```

<a id="ab0dae9b77818a8fee73d5b997cdc9a3c"></a>

### `MAX22017_GEN_INT_TMOUT_INT`

```c
#define MAX22017_GEN_INT_TMOUT_INT BIT(8)
```

<a id="a569d0198591bd1ac8cf3017985797161"></a>

### `MAX22017_GEN_INTEN_CONV_OVF_INTEN`

```c
#define MAX22017_GEN_INTEN_CONV_OVF_INTEN GENMASK(13, 12)
```

<a id="aabcebfeedc9571ed8d951bf876fe4231"></a>

### `MAX22017_GEN_INTEN_CRC_INTEN`

```c
#define MAX22017_GEN_INTEN_CRC_INTEN BIT(1)
```

<a id="a0ae1361d7e475c8a4eb2850d132a4498"></a>

### `MAX22017_GEN_INTEN_GPI_INTEN`

```c
#define MAX22017_GEN_INTEN_GPI_INTEN BIT(0)
```

<a id="a27665ac4ca4283876c7b0d82c68a0955"></a>

### `MAX22017_GEN_INTEN_HVDD_INTEN`

```c
#define MAX22017_GEN_INTEN_HVDD_INTEN BIT(9)
```

<a id="afaa5cf0a23d3b86bdb0aa8f64794a349"></a>

### `MAX22017_GEN_INTEN_OFF`

```c
#define MAX22017_GEN_INTEN_OFF 0x09
```

<a id="ab0d04e5d3b9a275e2f6d358d55f9ecec"></a>

### `MAX22017_GEN_INTEN_OPENWIRE_DTCT_INTEN`

```c
#define MAX22017_GEN_INTEN_OPENWIRE_DTCT_INTEN GENMASK(11, 10)
```

<a id="a9ec0c3a38830359ca2eebecc37275fe5"></a>

### `MAX22017_GEN_INTEN_OVC_INTEN`

```c
#define MAX22017_GEN_INTEN_OVC_INTEN GENMASK(3, 2)
```

<a id="a53365f203a2a2d4687807a7e709edfe7"></a>

### `MAX22017_GEN_INTEN_THSHDN_INTEN`

```c
#define MAX22017_GEN_INTEN_THSHDN_INTEN GENMASK(7, 6)
```

<a id="a9e9534a6244dc77b41b464be99997306"></a>

### `MAX22017_GEN_INTEN_THWRNG_INTEN`

```c
#define MAX22017_GEN_INTEN_THWRNG_INTEN GENMASK(5, 4)
```

<a id="a3759acb5df5704f36d97c159561efd10"></a>

### `MAX22017_GEN_INTEN_TMOUT_INTEN`

```c
#define MAX22017_GEN_INTEN_TMOUT_INTEN BIT(8)
```

<a id="a1693f93cd62731fe95c7ce1e1007d800"></a>

### `MAX22017_GEN_RST_CTRL_AO_COEFF_RELOAD`

```c
#define MAX22017_GEN_RST_CTRL_AO_COEFF_RELOAD GENMASK(15, 14)
```

<a id="ad544ab22f6ebf4a5a0d794a92145e2b5"></a>

### `MAX22017_GEN_RST_CTRL_GEN_RST`

```c
#define MAX22017_GEN_RST_CTRL_GEN_RST BIT(9)
```

<a id="a291a4ec441b4374377950c4c7f4badbf"></a>

### `MAX22017_GEN_RST_CTRL_OFF`

```c
#define MAX22017_GEN_RST_CTRL_OFF 0x0A
```

<a id="a269a0c9109afed5e63f29c9364d3931a"></a>

### `MAX22017_GEN_SERIAL_LSB_OFF`

```c
#define MAX22017_GEN_SERIAL_LSB_OFF 0x02
```

<a id="adbfda2921aaaf988e18efe7577ae8ed8"></a>

### `MAX22017_GEN_SERIAL_LSB_SERIAL_LSB`

```c
#define MAX22017_GEN_SERIAL_LSB_SERIAL_LSB GENMASK(15, 0)
```

<a id="a799bc9d76c76b5cfd4e0c4782e61c68d"></a>

### `MAX22017_GEN_SERIAL_MSB_OFF`

```c
#define MAX22017_GEN_SERIAL_MSB_OFF 0x01
```

<a id="a71543d48878b7290f2e81ecf1689d9c5"></a>

### `MAX22017_GEN_SERIAL_MSB_SERIAL_MSB`

```c
#define MAX22017_GEN_SERIAL_MSB_SERIAL_MSB GENMASK(15, 0)
```

<a id="a69b46acb4bf6ed483c1f453a77d7c257"></a>

### `MAX22017_LDAC_TOGGLE_TIME`

```c
#define MAX22017_LDAC_TOGGLE_TIME 200
```

<a id="a6420606c34753e82d867742e2f6ff846"></a>

### `MAX22017_MAX_CHANNEL`

```c
#define MAX22017_MAX_CHANNEL 2
```

<a id="aa1b178c2a60337d8b9dcfb4ac8315d14"></a>

### `MAX22017_SPI_TRANS_ADDR`

```c
#define MAX22017_SPI_TRANS_ADDR GENMASK(7, 1)
```

<a id="a0189fe593af9379781b6f63998b2d268"></a>

### `MAX22017_SPI_TRANS_DIR`

```c
#define MAX22017_SPI_TRANS_DIR BIT(0)
```

<a id="aa16b8b5dc1817df754d5228f4c335fc9"></a>

### `MAX22017_SPI_TRANS_PAYLOAD`

```c
#define MAX22017_SPI_TRANS_PAYLOAD GENMASK(15, 0)
```


## 47.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P103_max22017.h_源码浏览.md)
- [max22017_data](../device_power_control_model_reference/P023_max22017_data_结构体.md)
- [crc8](../data_utilities/P003_CRC计算接口.md#gaa614e73ee7484ca0424fa7d14a54bbb6)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [max22017_reg_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__max22017.html#ga7c051fa0697ae672a4dddbfa84059ad0)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [max22017_reg_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__max22017.html#gac4a4a29f7ae31af97f19d700264a604d)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P046_zephyr__net__lwm2m_path.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P048_zephyr__dt-bindings__dma__mchp-xec-dmac.h_文件参考.md)
