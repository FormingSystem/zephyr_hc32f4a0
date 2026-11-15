---
id: learning.zephyr-docs.api-source-pcie-hid-reference.page-7
title: mfd_ite_it8801.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mfd__ite__it8801_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_mfd\_ite\_it8801.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mfd__ite__it8801_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P220_zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考.md)。

## 7.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00098"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="amfd__ite__it8801_8h_html_a0e013175c1b2fd6ff3b62fb6eb3512ce"></a>
<a id="amfd__ite__it8801_8h_html_a50e301d4cfb9211625e851b0cc40f130"></a>
<a id="amfd__ite__it8801_8h_html_a722c1dbea588a3559edac523462dd755"></a>
<a id="amfd__ite__it8801_8h_html_a7273a553c04ac94c8adf244f1935b0ef"></a>
<a id="amfd__ite__it8801_8h_html_aeb61b0b4514fc757a016b8502ed58c09"></a>
<a id="amfd__ite__it8801_8h_html_aff5dcc74423dba3bad5693ec5e7d34be"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructi2c__dt__spec_html"></a>
<a id="astructit8801__mfd__callback_html"></a>
<a id="astructit8801__mfd__callback_html_a859a3813a936433024681903bc951b7d"></a>
<a id="astructit8801__mfd__callback_html_a9d4df8a0ba22f560bb799a1945a73592"></a>
<a id="astructit8801__mfd__callback_html_ab9b86565265e5f8c7409e44b559732ea"></a>
<a id="astructit8801__vendor__id__t_html"></a>
<a id="astructit8801__vendor__id__t_html_a384a9ea2a5d2d025473d672c2a0074ae"></a>
<a id="astructit8801__vendor__id__t_html_acb0a39c8e89593d6f45fe1089266bb85"></a>

```c
/*
 * Copyright (c) 2024 ITE Corporation. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MFD_ITE_IT8801_H_
#define ZEPHYR_INCLUDE_DRIVERS_MFD_ITE_IT8801_H_

#ifdef __cplusplus
extern "C" {
#endif

/*
 * IC clock and power management controller register fields
 */
/* 0xf9: Gather interrupt status register */
#define IT8801_REG_GISR             0xf9
#define IT8801_REG_MASK_GISR_GKSIIS BIT(6)
/* 0xfb: Gather interrupt enable control register */
#define IT8801_REG_GIECR            0xfb
#define IT8801_REG_MASK_GKSIIE      BIT(3)
#define IT8801_REG_MASK_GGPIOIE     BIT(2)

/*
 * General control register fields
 */
#define IT8801_REG_LBVIDR 0xfe
#define IT8801_REG_HBVIDR 0xff

struct it8801_vendor_id_t {
        uint8_t chip_id;
        uint8_t reg;
};

static const struct it8801_vendor_id_t it8801_id_verify[] = {
        {0x12, IT8801_REG_HBVIDR},
        {0x83, IT8801_REG_LBVIDR},
};

/*
 * SMbus interface register fields
 */
/* 0xfa: SMBus control register */
#define IT8801_REG_SMBCR    0xfa
#define IT8801_REG_MASK_ARE BIT(4)

/*
 * GPIO register fields
 */
#define IT8801_GPIOAFS_FUN1     0x0
#define IT8801_GPIOAFS_FUN2     0x01
#define IT8801_GPIOAFS_FUN3     0x02
/* GPIO control register */
/* GPIO direction */
#define IT8801_GPIODIR          BIT(5)
/* GPIO input and output type */
#define IT8801_GPIOIOT_OD       BIT(4)
#define IT8801_GPIOIOT_INT_FALL BIT(4)
#define IT8801_GPIOIOT_INT_RISE BIT(3)
/* GPIO polarity */
#define IT8801_GPIOPOL          BIT(2)
/* GPIO pull-down enable */
#define IT8801_GPIOPDE          BIT(1)
/* GPIO pull-up enable */
#define IT8801_GPIOPUE          BIT(0)

/*
 * Keyboard matrix scan controller register fields
 */
/* 0x40: Keyboard scan out mode control register */
#define IT8801_REG_MASK_KSOSDIC BIT(7)
#define IT8801_REG_MASK_KSE     BIT(6)
#define IT8801_REG_MASK_AKSOSC  BIT(5)

/*
 * PWM register fields
 */
#define PWM_IT8801_FREQ             32895
/* Control push-pull flag */
#define PWM_IT8801_PUSH_PULL        BIT(8)
/* 0x5f: PWM output open-drain disable register */
#define IT8801_REG_PWMODDSR         0x5f
/* PWM mode control register */
#define IT8801_PWMMCR_MCR_MASK      GENMASK(1, 0)
#define IT8801_PWMMCR_MCR_OFF       0
#define IT8801_PWMMCR_MCR_BLINKING  1
#define IT8801_PWMMCR_MCR_BREATHING 2
#define IT8801_PWMMCR_MCR_ON        3

/*
 * For IT8801 MFD alternate function controller
 */
#define IT8801_DT_INST_MFDCTRL(inst, idx) DT_INST_PHANDLE_BY_IDX(inst, mfdctrl, idx)

#define IT8801_DT_INST_MFDCTRL_LEN(inst) DT_INST_PROP_LEN_OR(inst, mfdctrl, 0)

#define IT8801_DEV_MFD(idx, inst)                                                                  \
        DEVICE_DT_GET(DT_PHANDLE(IT8801_DT_INST_MFDCTRL(inst, idx), altctrls))
#define IT8801_DEV_MFD_PIN(idx, inst)  DT_PHA(IT8801_DT_INST_MFDCTRL(inst, idx), altctrls, pin)
#define IT8801_DEV_MFD_FUNC(idx, inst) DT_PHA(IT8801_DT_INST_MFDCTRL(inst, idx), altctrls, alt_func)

#define IT8801_DT_MFD_ITEMS_FUNC(idx, inst)                                                        \
        {                                                                                          \
                .gpiocr = IT8801_DEV_MFD(idx, inst),                                               \
                .pin = IT8801_DEV_MFD_PIN(idx, inst),                                              \
                .alt_func = IT8801_DEV_MFD_FUNC(idx, inst),                                        \
        }

#define IT8801_DT_MFD_ITEMS_LIST(inst)                                                             \
        {LISTIFY(IT8801_DT_INST_MFDCTRL_LEN(inst),                                                 \
                IT8801_DT_MFD_ITEMS_FUNC, (,),                                                     \
                inst) }

/*
 * Configure alternate function pin
 */
int mfd_it8801_configure_pins(const struct i2c_dt_spec *i2c_dev, const struct device *dev,
                              uint8_t pin, uint8_t func);

/* Define the IT8801 MFD interrupt callback function handler */
typedef void (*it8801_callback_handler_t)(const struct device *dev);

struct it8801_mfd_callback {
        sys_snode_t node;
        it8801_callback_handler_t cb;
        const struct device *dev;
};
/* Register the interrupt of IT8801 MFD callback function */
void mfd_it8801_register_interrupt_callback(const struct device *mfd,
                                            struct it8801_mfd_callback *callback);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MFD_ITE_IT8801_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 ITE Corporation. All Rights Reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

芯片时钟与电源管理控制器（IC Clock and Power Management Controller）的寄存器字段。

### 注释 3：原第 17 行

`0xf9`：汇集中断状态寄存器（Gather Interrupt Status Register）。

### 注释 4：原第 20 行

`0xfb`：汇集中断使能控制寄存器（Gather Interrupt Enable Control Register）。

### 注释 5：原第 25 行

通用控制寄存器字段（General Control Register Fields）。

### 注释 6：原第 41 行

系统管理总线（SMBus）接口寄存器字段。

### 注释 7：原第 44 行

`0xfa`：SMBus 控制寄存器（Control Register）。

### 注释 8：原第 48 行

通用输入输出（GPIO）寄存器字段。

### 注释 9：原第 54 行

GPIO 控制寄存器（Control Register）。

### 注释 10：原第 55 行

GPIO 方向（Direction）。

### 注释 11：原第 57 行

GPIO 输入输出类型（Input and Output Type）。

### 注释 12：原第 61 行

GPIO 极性（Polarity）。

### 注释 13：原第 63 行

GPIO 下拉使能（Pull-down Enable）。

### 注释 14：原第 65 行

GPIO 上拉使能（Pull-up Enable）。

### 注释 15：原第 68 行

键盘矩阵扫描控制器（Keyboard Matrix Scan Controller）的寄存器字段。

### 注释 16：原第 71 行

`0x40`：键盘扫描输出模式控制寄存器（Keyboard Scan Out Mode Control Register）。

### 注释 17：原第 76 行

脉宽调制（PWM）寄存器字段。

### 注释 18：原第 80 行

控制推挽标志（Push-pull Flag）。

### 注释 19：原第 82 行

`0x5f`：PWM 输出开漏禁用寄存器（Open-drain Disable Register）。

### 注释 20：原第 84 行

PWM 模式控制寄存器（Mode Control Register）。

### 注释 21：原第 91 行

用于 IT8801 多功能设备（MFD）的复用功能控制器（Alternate Function Controller）。

### 注释 22：原第 115 行

配置复用功能引脚（Alternate Function Pin）。

### 注释 23：原第 121 行

定义 IT8801 多功能设备（MFD）的中断回调处理函数。

### 注释 24：原第 129 行

注册 IT8801 多功能设备（MFD）的中断回调函数。

### 注释 25：原第 137 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MFD_ITE_IT8801_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P220_zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考.md)
- [it8801_vendor_id_t](../device_power_control_model_reference/P022_it8801_vendor_id_t_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [chip_id](../device_power_control_model_reference/P022_it8801_vendor_id_t_结构体.md#acb0a39c8e89593d6f45fe1089266bb85)
- [reg](../device_power_control_model_reference/P022_it8801_vendor_id_t_结构体.md#a384a9ea2a5d2d025473d672c2a0074ae)
- [it8801_id_verify](../api_file_reference/P220_zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考.md#a0e013175c1b2fd6ff3b62fb6eb3512ce)
- [IT8801_REG_HBVIDR](../api_file_reference/P220_zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考.md#aff5dcc74423dba3bad5693ec5e7d34be)
- [IT8801_REG_LBVIDR](../api_file_reference/P220_zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考.md#a722c1dbea588a3559edac523462dd755)
- [mfd_it8801_configure_pins](../api_file_reference/P220_zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考.md#a7273a553c04ac94c8adf244f1935b0ef)
- [i2c_dt_spec](../hardware/P306_I2C设备树描述.md)
- [device](../device_reference/P002_设备对象结构.md)
- [it8801_callback_handler_t](../api_file_reference/P220_zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考.md#a50e301d4cfb9211625e851b0cc40f130)
- [it8801_mfd_callback](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md#ab9b86565265e5f8c7409e44b559732ea)
- [cb](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md#a859a3813a936433024681903bc951b7d)
- [dev](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md#a9d4df8a0ba22f560bb799a1945a73592)
- [mfd_it8801_register_interrupt_callback](../api_file_reference/P220_zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考.md#aeb61b0b4514fc757a016b8502ed58c09)
- [it8801_mfd_callback::cb](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md#a859a3813a936433024681903bc951b7d)
- [it8801_mfd_callback::dev](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md#a9d4df8a0ba22f560bb799a1945a73592)
- [it8801_mfd_callback::node](../device_power_control_model_reference/P021_it8801_mfd_callback_结构体.md#ab9b86565265e5f8c7409e44b559732ea)
- [it8801_vendor_id_t::reg](../device_power_control_model_reference/P022_it8801_vendor_id_t_结构体.md#a384a9ea2a5d2d025473d672c2a0074ae)
- [it8801_vendor_id_t::chip_id](../device_power_control_model_reference/P022_it8801_vendor_id_t_结构体.md#acb0a39c8e89593d6f45fe1089266bb85)

---

[上一章](P006_ite-intc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_sip_svc_controller.h_源码浏览.md)
