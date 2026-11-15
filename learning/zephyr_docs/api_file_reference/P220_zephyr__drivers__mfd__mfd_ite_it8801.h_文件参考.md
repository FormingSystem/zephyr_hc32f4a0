---
id: learning.zephyr-docs.api-file-reference.page-220
title: zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mfd__ite__it8801_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第220章\_zephyr\_\_drivers\_\_mfd\_\_mfd\_ite\_it8801.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mfd__ite__it8801_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 220.1\_数据结构（Data Structures）

<a id="r_it8801_5Fvendor_5Fid_5Ft"></a>

```c
struct it8801_vendor_id_t
```

相关声明：[it8801_vendor_id_t](../device_power_control_model_reference/P022_it8801_vendor_id_t_结构体.md)。

<a id="r_it8801_5Fmfd_5Fcallback"></a>

```c
struct it8801_mfd_callback
```

相关声明：[it8801_mfd_callback](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 220.2\_宏定义（Macros）

<a id="r_af769928fba020583c1aacafc3ef3f661"></a>

```c
#define IT8801_REG_GISR 0xf9
```

相关声明：[IT8801_REG_GISR](#af769928fba020583c1aacafc3ef3f661)。

<a id="r_a19097fcc347d262a8b970c447caeda8a"></a>

```c
#define IT8801_REG_MASK_GISR_GKSIIS BIT(6)
```

相关声明：[IT8801_REG_MASK_GISR_GKSIIS](#a19097fcc347d262a8b970c447caeda8a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_abb4de1bff69302bdff8e6420eaf0bdc1"></a>

```c
#define IT8801_REG_GIECR 0xfb
```

相关声明：[IT8801_REG_GIECR](#abb4de1bff69302bdff8e6420eaf0bdc1)。

<a id="r_a13e7af4eccface18b7e8d8fc782896b7"></a>

```c
#define IT8801_REG_MASK_GKSIIE BIT(3)
```

相关声明：[IT8801_REG_MASK_GKSIIE](#a13e7af4eccface18b7e8d8fc782896b7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ace92908cb46e1436279fb02216cd5021"></a>

```c
#define IT8801_REG_MASK_GGPIOIE BIT(2)
```

相关声明：[IT8801_REG_MASK_GGPIOIE](#ace92908cb46e1436279fb02216cd5021)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a722c1dbea588a3559edac523462dd755"></a>

```c
#define IT8801_REG_LBVIDR 0xfe
```

相关声明：[IT8801_REG_LBVIDR](#a722c1dbea588a3559edac523462dd755)。

<a id="r_aff5dcc74423dba3bad5693ec5e7d34be"></a>

```c
#define IT8801_REG_HBVIDR 0xff
```

相关声明：[IT8801_REG_HBVIDR](#aff5dcc74423dba3bad5693ec5e7d34be)。

<a id="r_af823bba3625871e586765885dc88ddc1"></a>

```c
#define IT8801_REG_SMBCR 0xfa
```

相关声明：[IT8801_REG_SMBCR](#af823bba3625871e586765885dc88ddc1)。

<a id="r_aa974608857370407d8fcbdbda3c474bd"></a>

```c
#define IT8801_REG_MASK_ARE BIT(4)
```

相关声明：[IT8801_REG_MASK_ARE](#aa974608857370407d8fcbdbda3c474bd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa93ce4f29ad9b4d9aeedfa3974c621b2"></a>

```c
#define IT8801_GPIOAFS_FUN1 0x0
```

相关声明：[IT8801_GPIOAFS_FUN1](#aa93ce4f29ad9b4d9aeedfa3974c621b2)。

<a id="r_a412905632e67c8ff0a00d6a366ad5bf2"></a>

```c
#define IT8801_GPIOAFS_FUN2 0x01
```

相关声明：[IT8801_GPIOAFS_FUN2](#a412905632e67c8ff0a00d6a366ad5bf2)。

<a id="r_a7a49cf897e723f57f7ce6aa030f890d5"></a>

```c
#define IT8801_GPIOAFS_FUN3 0x02
```

相关声明：[IT8801_GPIOAFS_FUN3](#a7a49cf897e723f57f7ce6aa030f890d5)。

<a id="r_a203d08ead5b60a5d51a66d550328aef6"></a>

```c
#define IT8801_GPIODIR BIT(5)
```

相关声明：[IT8801_GPIODIR](#a203d08ead5b60a5d51a66d550328aef6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_afb02201d261e416846e28af181ef75b6"></a>

```c
#define IT8801_GPIOIOT_OD BIT(4)
```

相关声明：[IT8801_GPIOIOT_OD](#afb02201d261e416846e28af181ef75b6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aca84886b619af7cd79d0b9cb27e16650"></a>

```c
#define IT8801_GPIOIOT_INT_FALL BIT(4)
```

相关声明：[IT8801_GPIOIOT_INT_FALL](#aca84886b619af7cd79d0b9cb27e16650)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad951ae2431f554ed5582ce74fa90c9f5"></a>

```c
#define IT8801_GPIOIOT_INT_RISE BIT(3)
```

相关声明：[IT8801_GPIOIOT_INT_RISE](#ad951ae2431f554ed5582ce74fa90c9f5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6a7ab8ecd064bf59f0b0d8ab3b5b2bf8"></a>

```c
#define IT8801_GPIOPOL BIT(2)
```

相关声明：[IT8801_GPIOPOL](#a6a7ab8ecd064bf59f0b0d8ab3b5b2bf8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1a516610506e0cbc06fe2b90748b8f19"></a>

```c
#define IT8801_GPIOPDE BIT(1)
```

相关声明：[IT8801_GPIOPDE](#a1a516610506e0cbc06fe2b90748b8f19)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a526c4b693f64f9592f59221019bbb1e1"></a>

```c
#define IT8801_GPIOPUE BIT(0)
```

相关声明：[IT8801_GPIOPUE](#a526c4b693f64f9592f59221019bbb1e1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a3ae2764c10f499cc3b9721eeb947b5b9"></a>

```c
#define IT8801_REG_MASK_KSOSDIC BIT(7)
```

相关声明：[IT8801_REG_MASK_KSOSDIC](#a3ae2764c10f499cc3b9721eeb947b5b9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a7664d5e95b800c5eb1dc728f72e7c232"></a>

```c
#define IT8801_REG_MASK_KSE BIT(6)
```

相关声明：[IT8801_REG_MASK_KSE](#a7664d5e95b800c5eb1dc728f72e7c232)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa5ffc9da4d8e8ae737735d39d6c97e7a"></a>

```c
#define IT8801_REG_MASK_AKSOSC BIT(5)
```

相关声明：[IT8801_REG_MASK_AKSOSC](#aa5ffc9da4d8e8ae737735d39d6c97e7a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a08d8cff79844be2e179d1742222e9e3c"></a>

```c
#define PWM_IT8801_FREQ 32895
```

相关声明：[PWM_IT8801_FREQ](#a08d8cff79844be2e179d1742222e9e3c)。

<a id="r_aab85a1fc0640f5eb243d098436d910fd"></a>

```c
#define PWM_IT8801_PUSH_PULL BIT(8)
```

相关声明：[PWM_IT8801_PUSH_PULL](#aab85a1fc0640f5eb243d098436d910fd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab6d8db36c938a43fd204fef6fc6bf28e"></a>

```c
#define IT8801_REG_PWMODDSR 0x5f
```

相关声明：[IT8801_REG_PWMODDSR](#ab6d8db36c938a43fd204fef6fc6bf28e)。

<a id="r_af943264d205ae66f691a934dc7598f79"></a>

```c
#define IT8801_PWMMCR_MCR_MASK GENMASK(1, 0)
```

相关声明：[IT8801_PWMMCR_MCR_MASK](#af943264d205ae66f691a934dc7598f79)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_adb356e532725450d445ff14258875f54"></a>

```c
#define IT8801_PWMMCR_MCR_OFF 0
```

相关声明：[IT8801_PWMMCR_MCR_OFF](#adb356e532725450d445ff14258875f54)。

<a id="r_a6609e354ecb0b18e376cbc58092f537a"></a>

```c
#define IT8801_PWMMCR_MCR_BLINKING 1
```

相关声明：[IT8801_PWMMCR_MCR_BLINKING](#a6609e354ecb0b18e376cbc58092f537a)。

<a id="r_a8e3d5f1c472ce31913e4053f3a7b1d70"></a>

```c
#define IT8801_PWMMCR_MCR_BREATHING 2
```

相关声明：[IT8801_PWMMCR_MCR_BREATHING](#a8e3d5f1c472ce31913e4053f3a7b1d70)。

<a id="r_a5fda70da82cd203efa8be58d437eab8b"></a>

```c
#define IT8801_PWMMCR_MCR_ON 3
```

相关声明：[IT8801_PWMMCR_MCR_ON](#a5fda70da82cd203efa8be58d437eab8b)。

<a id="r_aa9d6f1d7fc9b16a6137e1ccaed2ae497"></a>

```c
#define IT8801_DT_INST_MFDCTRL(inst, idx)
```

相关声明：[IT8801_DT_INST_MFDCTRL](#aa9d6f1d7fc9b16a6137e1ccaed2ae497)。

<a id="r_aa16440b852beb0b839c23312d817fca1"></a>

```c
#define IT8801_DT_INST_MFDCTRL_LEN(inst)
```

相关声明：[IT8801_DT_INST_MFDCTRL_LEN](#aa16440b852beb0b839c23312d817fca1)。

<a id="r_a8198cb9c55c8f068192dd715099d5d92"></a>

```c
#define IT8801_DEV_MFD(idx, inst)
```

相关声明：[IT8801_DEV_MFD](#a8198cb9c55c8f068192dd715099d5d92)。

<a id="r_aef92aa44c116c58f283f7185167085b6"></a>

```c
#define IT8801_DEV_MFD_PIN(idx, inst)
```

相关声明：[IT8801_DEV_MFD_PIN](#aef92aa44c116c58f283f7185167085b6)。

<a id="r_a7628a888ab7ba6187a7aadfb9f4af256"></a>

```c
#define IT8801_DEV_MFD_FUNC(idx, inst)
```

相关声明：[IT8801_DEV_MFD_FUNC](#a7628a888ab7ba6187a7aadfb9f4af256)。

<a id="r_afa5b636e82b01d8d9c631f1ccb6823ed"></a>

```c
#define IT8801_DT_MFD_ITEMS_FUNC(idx, inst)
```

相关声明：[IT8801_DT_MFD_ITEMS_FUNC](#afa5b636e82b01d8d9c631f1ccb6823ed)。

<a id="r_a3a2f4c469264e7dc90dc78ae22bd5147"></a>

```c
#define IT8801_DT_MFD_ITEMS_LIST(inst)
```

相关声明：[IT8801_DT_MFD_ITEMS_LIST](#a3a2f4c469264e7dc90dc78ae22bd5147)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 220.3\_类型定义（Typedefs）

<a id="r_a50e301d4cfb9211625e851b0cc40f130"></a>

```c
typedef void(* it8801_callback_handler_t) (const struct device *dev)
```

相关声明：[it8801_callback_handler_t](#a50e301d4cfb9211625e851b0cc40f130)、[device](../device_reference/P002_设备对象结构.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 220.4\_函数（Functions）

<a id="r_a7273a553c04ac94c8adf244f1935b0ef"></a>

```c
int mfd_it8801_configure_pins (const struct i2c_dt_spec *i2c_dev, const struct device *dev, uint8_t pin, uint8_t func)
```

相关声明：[mfd_it8801_configure_pins](#a7273a553c04ac94c8adf244f1935b0ef)、[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_aeb61b0b4514fc757a016b8502ed58c09"></a>

```c
void mfd_it8801_register_interrupt_callback (const struct device *mfd, struct it8801_mfd_callback *callback)
```

相关声明：[mfd_it8801_register_interrupt_callback](#aeb61b0b4514fc757a016b8502ed58c09)、[device](../device_reference/P002_设备对象结构.md)、[it8801_mfd_callback](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md)。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 220.5\_变量（Variables）

<a id="r_a0e013175c1b2fd6ff3b62fb6eb3512ce"></a>

```c
static const struct it8801_vendor_id_t it8801_id_verify []
```

相关声明：[it8801_vendor_id_t](../device_power_control_model_reference/P022_it8801_vendor_id_t_结构体.md)、[it8801_id_verify](#a0e013175c1b2fd6ff3b62fb6eb3512ce)。

## 220.6\_详细说明（Detailed Documentation）

<a id="a8198cb9c55c8f068192dd715099d5d92"></a>

### `IT8801_DEV_MFD`

```c
#define IT8801_DEV_MFD ( idx, inst )
```

展开值（Value）：

```c
DEVICE_DT_GET(DT_PHANDLE(IT8801_DT_INST_MFDCTRL(inst, idx), altctrls))
```

<a id="a7628a888ab7ba6187a7aadfb9f4af256"></a>

### `IT8801_DEV_MFD_FUNC`

```c
#define IT8801_DEV_MFD_FUNC ( idx, inst )
```

展开值（Value）：

```c
DT_PHA(IT8801_DT_INST_MFDCTRL(inst, idx), altctrls, alt_func)
```

<a id="aef92aa44c116c58f283f7185167085b6"></a>

### `IT8801_DEV_MFD_PIN`

```c
#define IT8801_DEV_MFD_PIN ( idx, inst )
```

展开值（Value）：

```c
DT_PHA(IT8801_DT_INST_MFDCTRL(inst, idx), altctrls, pin)
```

<a id="aa9d6f1d7fc9b16a6137e1ccaed2ae497"></a>

### `IT8801_DT_INST_MFDCTRL`

```c
#define IT8801_DT_INST_MFDCTRL ( inst, idx )
```

展开值（Value）：

```c
DT_INST_PHANDLE_BY_IDX(inst, mfdctrl, idx)
```

<a id="aa16440b852beb0b839c23312d817fca1"></a>

### `IT8801_DT_INST_MFDCTRL_LEN`

```c
#define IT8801_DT_INST_MFDCTRL_LEN ( inst)
```

展开值（Value）：

```c
DT_INST_PROP_LEN_OR(inst, mfdctrl, 0)
```

<a id="afa5b636e82b01d8d9c631f1ccb6823ed"></a>

### `IT8801_DT_MFD_ITEMS_FUNC`

```c
#define IT8801_DT_MFD_ITEMS_FUNC ( idx, inst )
```

展开值（Value）：

```c
{                                                                                          \
        .gpiocr = IT8801_DEV_MFD(idx, inst),                                               \
        .pin = IT8801_DEV_MFD_PIN(idx, inst),                                              \
        .alt_func = IT8801_DEV_MFD_FUNC(idx, inst),                                        \
}
```

<a id="a3a2f4c469264e7dc90dc78ae22bd5147"></a>

### `IT8801_DT_MFD_ITEMS_LIST`

```c
#define IT8801_DT_MFD_ITEMS_LIST ( inst)
```

展开值（Value）：

```c
{LISTIFY(IT8801_DT_INST_MFDCTRL_LEN(inst),                                                 \
        IT8801_DT_MFD_ITEMS_FUNC, (,),                                                     \
        inst) }
```

<a id="aa93ce4f29ad9b4d9aeedfa3974c621b2"></a>

### `IT8801_GPIOAFS_FUN1`

```c
#define IT8801_GPIOAFS_FUN1 0x0
```

<a id="a412905632e67c8ff0a00d6a366ad5bf2"></a>

### `IT8801_GPIOAFS_FUN2`

```c
#define IT8801_GPIOAFS_FUN2 0x01
```

<a id="a7a49cf897e723f57f7ce6aa030f890d5"></a>

### `IT8801_GPIOAFS_FUN3`

```c
#define IT8801_GPIOAFS_FUN3 0x02
```

<a id="a203d08ead5b60a5d51a66d550328aef6"></a>

### `IT8801_GPIODIR`

```c
#define IT8801_GPIODIR BIT(5)
```

<a id="aca84886b619af7cd79d0b9cb27e16650"></a>

### `IT8801_GPIOIOT_INT_FALL`

```c
#define IT8801_GPIOIOT_INT_FALL BIT(4)
```

<a id="ad951ae2431f554ed5582ce74fa90c9f5"></a>

### `IT8801_GPIOIOT_INT_RISE`

```c
#define IT8801_GPIOIOT_INT_RISE BIT(3)
```

<a id="afb02201d261e416846e28af181ef75b6"></a>

### `IT8801_GPIOIOT_OD`

```c
#define IT8801_GPIOIOT_OD BIT(4)
```

<a id="a1a516610506e0cbc06fe2b90748b8f19"></a>

### `IT8801_GPIOPDE`

```c
#define IT8801_GPIOPDE BIT(1)
```

<a id="a6a7ab8ecd064bf59f0b0d8ab3b5b2bf8"></a>

### `IT8801_GPIOPOL`

```c
#define IT8801_GPIOPOL BIT(2)
```

<a id="a526c4b693f64f9592f59221019bbb1e1"></a>

### `IT8801_GPIOPUE`

```c
#define IT8801_GPIOPUE BIT(0)
```

<a id="a6609e354ecb0b18e376cbc58092f537a"></a>

### `IT8801_PWMMCR_MCR_BLINKING`

```c
#define IT8801_PWMMCR_MCR_BLINKING 1
```

<a id="a8e3d5f1c472ce31913e4053f3a7b1d70"></a>

### `IT8801_PWMMCR_MCR_BREATHING`

```c
#define IT8801_PWMMCR_MCR_BREATHING 2
```

<a id="af943264d205ae66f691a934dc7598f79"></a>

### `IT8801_PWMMCR_MCR_MASK`

```c
#define IT8801_PWMMCR_MCR_MASK GENMASK(1, 0)
```

<a id="adb356e532725450d445ff14258875f54"></a>

### `IT8801_PWMMCR_MCR_OFF`

```c
#define IT8801_PWMMCR_MCR_OFF 0
```

<a id="a5fda70da82cd203efa8be58d437eab8b"></a>

### `IT8801_PWMMCR_MCR_ON`

```c
#define IT8801_PWMMCR_MCR_ON 3
```

<a id="abb4de1bff69302bdff8e6420eaf0bdc1"></a>

### `IT8801_REG_GIECR`

```c
#define IT8801_REG_GIECR 0xfb
```

<a id="af769928fba020583c1aacafc3ef3f661"></a>

### `IT8801_REG_GISR`

```c
#define IT8801_REG_GISR 0xf9
```

<a id="aff5dcc74423dba3bad5693ec5e7d34be"></a>

### `IT8801_REG_HBVIDR`

```c
#define IT8801_REG_HBVIDR 0xff
```

<a id="a722c1dbea588a3559edac523462dd755"></a>

### `IT8801_REG_LBVIDR`

```c
#define IT8801_REG_LBVIDR 0xfe
```

<a id="aa5ffc9da4d8e8ae737735d39d6c97e7a"></a>

### `IT8801_REG_MASK_AKSOSC`

```c
#define IT8801_REG_MASK_AKSOSC BIT(5)
```

<a id="aa974608857370407d8fcbdbda3c474bd"></a>

### `IT8801_REG_MASK_ARE`

```c
#define IT8801_REG_MASK_ARE BIT(4)
```

<a id="ace92908cb46e1436279fb02216cd5021"></a>

### `IT8801_REG_MASK_GGPIOIE`

```c
#define IT8801_REG_MASK_GGPIOIE BIT(2)
```

<a id="a19097fcc347d262a8b970c447caeda8a"></a>

### `IT8801_REG_MASK_GISR_GKSIIS`

```c
#define IT8801_REG_MASK_GISR_GKSIIS BIT(6)
```

<a id="a13e7af4eccface18b7e8d8fc782896b7"></a>

### `IT8801_REG_MASK_GKSIIE`

```c
#define IT8801_REG_MASK_GKSIIE BIT(3)
```

<a id="a7664d5e95b800c5eb1dc728f72e7c232"></a>

### `IT8801_REG_MASK_KSE`

```c
#define IT8801_REG_MASK_KSE BIT(6)
```

<a id="a3ae2764c10f499cc3b9721eeb947b5b9"></a>

### `IT8801_REG_MASK_KSOSDIC`

```c
#define IT8801_REG_MASK_KSOSDIC BIT(7)
```

<a id="ab6d8db36c938a43fd204fef6fc6bf28e"></a>

### `IT8801_REG_PWMODDSR`

```c
#define IT8801_REG_PWMODDSR 0x5f
```

<a id="af823bba3625871e586765885dc88ddc1"></a>

### `IT8801_REG_SMBCR`

```c
#define IT8801_REG_SMBCR 0xfa
```

<a id="a08d8cff79844be2e179d1742222e9e3c"></a>

### `PWM_IT8801_FREQ`

```c
#define PWM_IT8801_FREQ 32895
```

<a id="aab85a1fc0640f5eb243d098436d910fd"></a>

### `PWM_IT8801_PUSH_PULL`

```c
#define PWM_IT8801_PUSH_PULL BIT(8)
```

<a id="a50e301d4cfb9211625e851b0cc40f130"></a>

### `it8801_callback_handler_t`

```c
typedef void(* it8801_callback_handler_t) (const struct device *dev)
```

<a id="a7273a553c04ac94c8adf244f1935b0ef"></a>

### `mfd_it8801_configure_pins()`

```c
int mfd_it8801_configure_pins ( const struct i2c_dt_spec * i2c_dev, const struct device * dev, uint8_t pin, uint8_t func )
```

<a id="aeb61b0b4514fc757a016b8502ed58c09"></a>

### `mfd_it8801_register_interrupt_callback()`

```c
void mfd_it8801_register_interrupt_callback ( const struct device * mfd, struct it8801_mfd_callback * callback )
```

<a id="a0e013175c1b2fd6ff3b62fb6eb3512ce"></a>

### `it8801_id_verify`

```c
const struct it8801_vendor_id_t it8801_id_verify[]
```

声明属性：`static`。

原始示例（Example）：

```c
                                      = {
        {0x12, 0xff },
        {0x83, 0xfe },
}
```


## 220.7\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/mfd__ite__it8801_8h_source.html)
- [it8801_vendor_id_t](../device_power_control_model_reference/P022_it8801_vendor_id_t_结构体.md)
- [it8801_mfd_callback](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [device](../device_reference/P002_设备对象结构.md)
- [i2c_dt_spec](../hardware/P306_I2C设备树描述.md)
- [uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_PHANDLE](../dt_property_reference/P001_设备树属性读取宏.md#ga7bd77c49472ba4547d87f00f40fd7171)
- [DT_PHA](../dt_property_reference/P001_设备树属性读取宏.md#gacef5921973a55433161fe0be3f8f628d)
- [DT_INST_PHANDLE_BY_IDX](../dt_instance_reference/P001_设备树驱动实例宏.md#ga10d93a1f9a9f5e225508c4c383654b1c)
- [DT_INST_PROP_LEN_OR](../dt_instance_reference/P001_设备树驱动实例宏.md#ga9be8fdcc8c4032748b47f497efa19173)
- [LISTIFY](../util_reference/P001_通用工具公共接口.md#ga81cbc0233cf73048d65b76f716653af6)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-generic-prop_html_ga7bd77c49472ba4547d87f00f40fd7171"></a>
<a id="amfd__ite__it8801_8h_html_aa9d6f1d7fc9b16a6137e1ccaed2ae497"></a>
<a id="agroup__devicetree-generic-prop_html_gacef5921973a55433161fe0be3f8f628d"></a>
<a id="agroup__devicetree-inst_html_ga10d93a1f9a9f5e225508c4c383654b1c"></a>
<a id="agroup__devicetree-inst_html_ga9be8fdcc8c4032748b47f497efa19173"></a>
<a id="amfd__ite__it8801_8h_html_a7628a888ab7ba6187a7aadfb9f4af256"></a>
<a id="amfd__ite__it8801_8h_html_a8198cb9c55c8f068192dd715099d5d92"></a>
<a id="amfd__ite__it8801_8h_html_aef92aa44c116c58f283f7185167085b6"></a>
<a id="agroup__sys-util_html_ga81cbc0233cf73048d65b76f716653af6"></a>
<a id="amfd__ite__it8801_8h_html_aa16440b852beb0b839c23312d817fca1"></a>
<a id="amfd__ite__it8801_8h_html_afa5b636e82b01d8d9c631f1ccb6823ed"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P219_zephyr__drivers__mfd__max31790.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P221_zephyr__drivers__mic_privacy__intel__mic_privacy.h_文件参考.md)
