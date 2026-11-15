---
id: learning.zephyr-docs.api-file-system-power-reference.page-8
title: zephyr__drivers__mfd__adp5360.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2adp5360_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_mfd\_\_adp5360.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2adp5360_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_child_5Finterrupt_5Fcallback"></a>

```c
struct child_interrupt_callback
```

相关声明：[child_interrupt_callback](../platform_security_model_reference/P001_child_interrupt_callback_结构体.md)。

子设备中断（Child Device Interrupt）的回调结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.2\_类型定义（Typedefs）

<a id="r_ga6fbc5513a83d209b35166a3c9e50412f"></a>

```c
typedef void(* mfd_adp5360_interrupt_callback) (const struct device *dev, void *user_data)
```

相关声明：[mfd_adp5360_interrupt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga6fbc5513a83d209b35166a3c9e50412f)、[device](../device_reference/P002_设备对象结构.md)。

ADP5360 多功能设备（MFD）中断的中断回调函数类型（Interrupt Callback Function Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.3\_枚举（Enumerations）

<a id="r_gae4d56fd30130dc4f332ecf43465a1558"></a>

```c
enum child_dev { ADP5360_DEV_REG = 0 , ADP5360_DEV_CHG , ADP5360_DEV_FG , ADP5360_DEV_MAX }
```

相关声明：[child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)、[ADP5360_DEV_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ggae4d56fd30130dc4f332ecf43465a1558a83e6800b4416bf2eef91f8639cc503a7)、[ADP5360_DEV_CHG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ggae4d56fd30130dc4f332ecf43465a1558a57a9b20b6a6d336cefd22f9eb0dc1608)、[ADP5360_DEV_FG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ggae4d56fd30130dc4f332ecf43465a1558ab2f34f44d1fd49f77f26bddca8a86178)、[ADP5360_DEV_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ggae4d56fd30130dc4f332ecf43465a1558a9789d1642be7ad8efc0f137940051177)。

ADP5360 的子设备（Child Device）。

<a id="r_ga20968112912ecd3310d86c765c3f1bf5"></a>

```c
enum adp5360_interrupt_type { ADP5360_INTERRUPT_VBUS_VOLTAGE_THRESHOLD = 0 , ADP5360_INTERRUPT_CHARGER_MODE_CHANGE , ADP5360_INTERRUPT_BAT_VOLTAGE_THRESHOLD , ADP5360_INTERRUPT_TEMP_THRESHOLD , ADP5360_INTERRUPT_BAT_PROTECTION , ADP5360_INTERRUPT_ADPICHG , ADP5360_INTERRUPT_SOC_ACM , ADP5360_INTERRUPT_SOC_LOW , ADP5360_INTERRUPT_BUCKBSTPGOOD , ADP5360_INTERRUPT_BUCKPGOOD , ADP5360_INTERRUPT_WATCHDOG_TIMEOUT , ADP5360_INTERRUPT_MANUAL_RESET }
```

相关声明：[adp5360_interrupt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga20968112912ecd3310d86c765c3f1bf5)、[ADP5360_INTERRUPT_VBUS_VOLTAGE_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a2d82f2df8d1c570341e9f808640280f8)、[ADP5360_INTERRUPT_CHARGER_MODE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5aa0f5963e739ebefc5606990cb0469221)、[ADP5360_INTERRUPT_BAT_VOLTAGE_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5ad19b0cc2d535ce6e1fcebcc245c7ffbe)、[ADP5360_INTERRUPT_TEMP_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a3687e52a9fbc8b37993c4ca0ac6167d1)、[ADP5360_INTERRUPT_BAT_PROTECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5af9ab20ec2fc2d77951b0a9c2ca0c2b03)、[ADP5360_INTERRUPT_ADPICHG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a5e593064c54c23b26b16b5d6659fe825)、[ADP5360_INTERRUPT_SOC_ACM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a52c5bc7dda075c519b62f20b5ab9a8a3)、[ADP5360_INTERRUPT_SOC_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5abfc06aa3e683a861c69c3aab225c6a9d)、[ADP5360_INTERRUPT_BUCKBSTPGOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a48232f5dd216eaf2cb5e9488dcb642da)、[ADP5360_INTERRUPT_BUCKPGOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a5953a24e456e38779bc58d8881a3af3f)、[ADP5360_INTERRUPT_WATCHDOG_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a637aa89277e23fe88b57c9a01cb1d27d)、[ADP5360_INTERRUPT_MANUAL_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a02114e766195cd67618dae2d4b642755)。

ADP5360 中断类型（Interrupt Types）。

<a id="r_ga316db7c3085870260884952c9f60befc"></a>

```c
enum pgood_pin { ADP5360_PGOOD1 = 1 , ADP5360_PGOOD2 }
```

相关声明：[pgood_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga316db7c3085870260884952c9f60befc)、[ADP5360_PGOOD1](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga316db7c3085870260884952c9f60befca79acf84c38be5a0f815e8f61aef4be39)、[ADP5360_PGOOD2](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga316db7c3085870260884952c9f60befcad8bb0bdb18f11776b272f8087076fafd)。

电源良好（Power Good）引脚选择。

<a id="r_ga65e24906cba328faa2291b610d787021"></a>

```c
enum adp5360_pgood_status_type { ADP5360_PGOOD_STATUS_CHARGE_COMPLETE = 0 , ADP5360_PGOOD_STATUS_VBUS_OK , ADP5360_PGOOD_STATUS_BATTERY_OK , ADP5360_PGOOD_STATUS_VOUT2_OK , ADP5360_PGOOD_STATUS_VOUT1_OK }
```

相关声明：[adp5360_pgood_status_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga65e24906cba328faa2291b610d787021)、[ADP5360_PGOOD_STATUS_CHARGE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021aa261a4a2051c3dafff9d323a29ca8061)、[ADP5360_PGOOD_STATUS_VBUS_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021af685925abeb058cefdfd52ea7f911f06)、[ADP5360_PGOOD_STATUS_BATTERY_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021a676da5d1a34c65a8b190315a6fbaa37a)、[ADP5360_PGOOD_STATUS_VOUT2_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021aaf613fb55ae41397a751e0f6bf6efc75)、[ADP5360_PGOOD_STATUS_VOUT1_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021a17c1c016f43c1b9d45563e590df952cf)。

电源良好状态（Power Good Status）类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_gaa13607c11a36f6db7dee74ef3b9f1666"></a>

```c
int mfd_adp5360_software_reset (const struct device *dev)
```

相关声明：[mfd_adp5360_software_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gaa13607c11a36f6db7dee74ef3b9f1666)、[device](../device_reference/P002_设备对象结构.md)。

对 ADP5360 设备执行软件复位（Software Reset）。

<a id="r_gad7790331ffd4bb128ee7fd393585f68a"></a>

```c
int mfd_adp5360_hardware_reset (const struct device *dev)
```

相关声明：[mfd_adp5360_hardware_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gad7790331ffd4bb128ee7fd393585f68a)、[device](../device_reference/P002_设备对象结构.md)。

对 ADP5360 设备执行硬件复位（Hardware Reset）。

<a id="r_ga7cdbdf8cca5956dd6a996ab36c0fbcc8"></a>

```c
int mfd_adp5360_reset_trigger_set (const struct device *dev, mfd_adp5360_interrupt_callback handler, void *user_data)
```

相关声明：[mfd_adp5360_reset_trigger_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga7cdbdf8cca5956dd6a996ab36c0fbcc8)、[device](../device_reference/P002_设备对象结构.md)、[mfd_adp5360_interrupt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga6fbc5513a83d209b35166a3c9e50412f)。

为复位中断事件（Reset Interrupt Events）注册回调。

<a id="r_ga529e06b2830a759cea08e55e211a4a1f"></a>

```c
int mfd_adp5360_pgood_trigger_set (const struct device *dev, enum pgood_pin pin, enum adp5360_pgood_status_type type, mfd_adp5360_interrupt_callback handler, void *user_data)
```

相关声明：[mfd_adp5360_pgood_trigger_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga529e06b2830a759cea08e55e211a4a1f)、[device](../device_reference/P002_设备对象结构.md)、[pgood_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga316db7c3085870260884952c9f60befc)、[adp5360_pgood_status_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga65e24906cba328faa2291b610d787021)、[mfd_adp5360_interrupt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga6fbc5513a83d209b35166a3c9e50412f)。

为电源良好（PGOOD）引脚状态变化注册回调。

<a id="r_ga173ff73fd60260d44eda16e0f26ea270"></a>

```c
int mfd_adp5360_interrupt_trigger_set (const struct device *dev, enum adp5360_interrupt_type type, mfd_adp5360_interrupt_callback handler, void *user_data)
```

相关声明：[mfd_adp5360_interrupt_trigger_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga173ff73fd60260d44eda16e0f26ea270)、[device](../device_reference/P002_设备对象结构.md)、[adp5360_interrupt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga20968112912ecd3310d86c765c3f1bf5)、[mfd_adp5360_interrupt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga6fbc5513a83d209b35166a3c9e50412f)。

为指定中断类型（Interrupt Type）注册回调。

<a id="r_gaf5cd0d182605424e3baff76d75295ba3"></a>

```c
int mfd_adp5360_shipment_mode_enable (const struct device *dev)
```

相关声明：[mfd_adp5360_shipment_mode_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gaf5cd0d182605424e3baff76d75295ba3)、[device](../device_reference/P002_设备对象结构.md)。

启用 ADP5360 设备的运输模式（Shipment Mode）。

<a id="r_ga1681f46d19ac7cbe61f5b9fd91169c00"></a>

```c
int mfd_adp5360_shipment_mode_disable (const struct device *dev)
```

相关声明：[mfd_adp5360_shipment_mode_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga1681f46d19ac7cbe61f5b9fd91169c00)、[device](../device_reference/P002_设备对象结构.md)。

禁用 ADP5360 设备的运输模式（Shipment Mode）。


## 8.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P159_adp5360.h_源码浏览.md)
- [child_interrupt_callback](../platform_security_model_reference/P001_child_interrupt_callback_结构体.md)
- [mfd_adp5360_interrupt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga6fbc5513a83d209b35166a3c9e50412f)
- [device](../device_reference/P002_设备对象结构.md)
- [child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)
- [ADP5360_DEV_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ggae4d56fd30130dc4f332ecf43465a1558a83e6800b4416bf2eef91f8639cc503a7)
- [ADP5360_DEV_CHG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ggae4d56fd30130dc4f332ecf43465a1558a57a9b20b6a6d336cefd22f9eb0dc1608)
- [ADP5360_DEV_FG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ggae4d56fd30130dc4f332ecf43465a1558ab2f34f44d1fd49f77f26bddca8a86178)
- [ADP5360_DEV_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ggae4d56fd30130dc4f332ecf43465a1558a9789d1642be7ad8efc0f137940051177)
- [adp5360_interrupt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga20968112912ecd3310d86c765c3f1bf5)
- [ADP5360_INTERRUPT_VBUS_VOLTAGE_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a2d82f2df8d1c570341e9f808640280f8)
- [ADP5360_INTERRUPT_CHARGER_MODE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5aa0f5963e739ebefc5606990cb0469221)
- [ADP5360_INTERRUPT_BAT_VOLTAGE_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5ad19b0cc2d535ce6e1fcebcc245c7ffbe)
- [ADP5360_INTERRUPT_TEMP_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a3687e52a9fbc8b37993c4ca0ac6167d1)
- [ADP5360_INTERRUPT_BAT_PROTECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5af9ab20ec2fc2d77951b0a9c2ca0c2b03)
- [ADP5360_INTERRUPT_ADPICHG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a5e593064c54c23b26b16b5d6659fe825)
- [ADP5360_INTERRUPT_SOC_ACM](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a52c5bc7dda075c519b62f20b5ab9a8a3)
- [ADP5360_INTERRUPT_SOC_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5abfc06aa3e683a861c69c3aab225c6a9d)
- [ADP5360_INTERRUPT_BUCKBSTPGOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a48232f5dd216eaf2cb5e9488dcb642da)
- [ADP5360_INTERRUPT_BUCKPGOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a5953a24e456e38779bc58d8881a3af3f)
- [ADP5360_INTERRUPT_WATCHDOG_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a637aa89277e23fe88b57c9a01cb1d27d)
- [ADP5360_INTERRUPT_MANUAL_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga20968112912ecd3310d86c765c3f1bf5a02114e766195cd67618dae2d4b642755)
- [pgood_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga316db7c3085870260884952c9f60befc)
- [ADP5360_PGOOD1](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga316db7c3085870260884952c9f60befca79acf84c38be5a0f815e8f61aef4be39)
- [ADP5360_PGOOD2](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga316db7c3085870260884952c9f60befcad8bb0bdb18f11776b272f8087076fafd)
- [adp5360_pgood_status_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga65e24906cba328faa2291b610d787021)
- [ADP5360_PGOOD_STATUS_CHARGE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021aa261a4a2051c3dafff9d323a29ca8061)
- [ADP5360_PGOOD_STATUS_VBUS_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021af685925abeb058cefdfd52ea7f911f06)
- [ADP5360_PGOOD_STATUS_BATTERY_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021a676da5d1a34c65a8b190315a6fbaa37a)
- [ADP5360_PGOOD_STATUS_VOUT2_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021aaf613fb55ae41397a751e0f6bf6efc75)
- [ADP5360_PGOOD_STATUS_VOUT1_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gga65e24906cba328faa2291b610d787021a17c1c016f43c1b9d45563e590df952cf)
- [mfd_adp5360_software_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gaa13607c11a36f6db7dee74ef3b9f1666)
- [mfd_adp5360_hardware_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gad7790331ffd4bb128ee7fd393585f68a)
- [mfd_adp5360_reset_trigger_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga7cdbdf8cca5956dd6a996ab36c0fbcc8)
- [mfd_adp5360_pgood_trigger_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga529e06b2830a759cea08e55e211a4a1f)
- [mfd_adp5360_interrupt_trigger_set](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga173ff73fd60260d44eda16e0f26ea270)
- [mfd_adp5360_shipment_mode_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gaf5cd0d182605424e3baff76d75295ba3)
- [mfd_adp5360_shipment_mode_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#ga1681f46d19ac7cbe61f5b9fd91169c00)

---

[上一章](P007_zephyr__net__dplpmtud.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__sensor__icm4268x.h_文件参考.md)
