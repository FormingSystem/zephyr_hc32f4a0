---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-7
title: zephyr__drivers__misc__max2221x__max2221x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/misc_2max2221x_2max2221x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_misc\_\_max2221x\_\_max2221x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/misc_2max2221x_2max2221x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAX2221X杂项（MISC）驱动的公共API。

查看此文件的源码。

<a id="details"></a>

MAX2221X杂项（MISC）驱动的公共API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="define-members-0"></a>

### MAX2221X 斜坡使能／禁用掩码（MAX2221X Ramp Enable/Disable Masks）

<a id="r_gae933f32f8cf7328dca2afb7f344dcb29"></a>

```c
#define MAX2221X_RAMP_DOWN_MASK BIT(2)
```

相关声明：[MAX2221X_RAMP_DOWN_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gae933f32f8cf7328dca2afb7f344dcb29)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

下降斜坡使能掩码（Ramp-down Enable Mask）。

<a id="r_gacb47da8940b93285c56693dee2aca071"></a>

```c
#define MAX2221X_RAMP_MID_MASK BIT(1)
```

相关声明：[MAX2221X_RAMP_MID_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gacb47da8940b93285c56693dee2aca071)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

中间斜坡使能掩码（Ramp-middle Enable Mask）。

<a id="r_ga73042e2ff448d10d2b36135f1f2fd27e"></a>

```c
#define MAX2221X_RAMP_UP_MASK BIT(0)
```

相关声明：[MAX2221X_RAMP_UP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga73042e2ff448d10d2b36135f1f2fd27e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

上升斜坡使能掩码（Ramp-up Enable Mask）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.2\_枚举（Enumerations）

<a id="r_ga8f702fe056959c707d495a5b49ec7647"></a>

```c
enum max2221x_master_chop_freq { MAX2221X_FREQ_100KHZ = 0 , MAX2221X_FREQ_80KHZ , MAX2221X_FREQ_60KHZ , MAX2221X_FREQ_50KHZ , MAX2221X_FREQ_40KHZ , MAX2221X_FREQ_30KHZ , MAX2221X_FREQ_25KHZ , MAX2221X_FREQ_20KHZ , MAX2221X_FREQ_15KHZ , MAX2221X_FREQ_10KHZ , MAX2221X_FREQ_7500HZ , MAX2221X_FREQ_5000HZ , MAX2221X_FREQ_2500HZ , MAX2221X_FREQ_INVALID }
```

相关声明：[max2221x_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga8f702fe056959c707d495a5b49ec7647)、[MAX2221X_FREQ_100KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab689b993d9fa98c5bf140162723d2feb)、[MAX2221X_FREQ_80KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1a478348731bd456313912f6b4a59f1f)、[MAX2221X_FREQ_60KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a93bf099ae22e26de9885c76bc8428eb8)、[MAX2221X_FREQ_50KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1710af28d11faf44c423f2f771f02980)、[MAX2221X_FREQ_40KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a34a90a18c91e8e6f547c0788d4061612)、[MAX2221X_FREQ_30KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab4e2229b6516ea4f7278fa2931f262ed)、[MAX2221X_FREQ_25KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a8a11aacff6d925230f8719508b432cef)、[MAX2221X_FREQ_20KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a5cdbdb4c266cca9ae859f20dc0187a15)、[MAX2221X_FREQ_15KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647aa39e41621ac0f7f7073d95cfa18c99a4)、[MAX2221X_FREQ_10KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647abcaa72d42d74f8054480c73bf3fa61f5)、[MAX2221X_FREQ_7500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a208bff3bc2c214ea84404ba49c1037cb)、[MAX2221X_FREQ_5000HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a0e56c34ed02843a63bbcfe0d219b2dbc)、[MAX2221X_FREQ_2500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a30dbf5e8aa5f7aa61cff6cf7391e39c9)、[MAX2221X_FREQ_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a2bfeae761213ed84221a6bda013599aa)。

主斩波频率（Master Chopping Frequency）选项。

<a id="r_ga41010c75c9cb6ed23e06cfec0ebbe413"></a>

```c
enum max2221x_individual_chop_freq { MAX2221X_FREQ_M = 0 , MAX2221X_FREQ_M_2 , MAX2221X_FREQ_M_4 , MAX2221X_FREQ_M_8 , MAX2221X_FREQ_M_INVALID }
```

相关声明：[max2221x_individual_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga41010c75c9cb6ed23e06cfec0ebbe413)、[MAX2221X_FREQ_M](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a4cee57aef5be5d79919513fea3891490)、[MAX2221X_FREQ_M_2](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a120c21fdf16a48795233bae403a0c3f1)、[MAX2221X_FREQ_M_4](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a84119a5bb314c03760637ebb05a7f16a)、[MAX2221X_FREQ_M_8](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413ac0955ebf50e1c3d7a51e6aa42e008cfd)、[MAX2221X_FREQ_M_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413af6f9cae164f70b5fc9a7003e526d15b2)。

独立通道斩波频率分频系数（Chopping Frequency Divisor）选项。

<a id="r_ga399738e28a4b7c309137d674e433ccb6"></a>

```c
enum max2221x_fault_pin_masks { MAX2221X_FAULT_PIN_UVM = 0 , MAX2221X_FAULT_PIN_COMF , MAX2221X_FAULT_PIN_DPM , MAX2221X_FAULT_PIN_HHF , MAX2221X_FAULT_PIN_OLF , MAX2221X_FAULT_PIN_OCP , MAX2221X_FAULT_PIN_OVT , MAX2221X_FAULT_PIN_INVALID }
```

相关声明：[max2221x_fault_pin_masks](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga399738e28a4b7c309137d674e433ccb6)、[MAX2221X_FAULT_PIN_UVM](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a9cf6ad6bb71092f7e28eb7de91e92a51)、[MAX2221X_FAULT_PIN_COMF](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a9492bcaf6e4e5e41bca5d156b7cbde92)、[MAX2221X_FAULT_PIN_DPM](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a12806ad411905619c15ed7cc603cdb36)、[MAX2221X_FAULT_PIN_HHF](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a28bb4d3f65348762116f5a14b6a4614f)、[MAX2221X_FAULT_PIN_OLF](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a5dcb7a29041c5ec4b399795cf59db322)、[MAX2221X_FAULT_PIN_OCP](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6aae654309f343b46f117327afe025c789)、[MAX2221X_FAULT_PIN_OVT](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a1f2abcecc1b2ad5092322034797fa391)、[MAX2221X_FAULT_PIN_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a41a39797fc9dfc70c31f7fa08d083354)。

故障引脚掩码定义（Fault Pin Mask Definitions）。

<a id="r_gafced3b909c7963f0711bb23eecb4b538"></a>

```c
enum max2221x_vdr_mode { MAX2221X_VDR_MODE_NORMAL = 0 , MAX2221X_VDR_MODE_DUTY , MAX2221X_VDR_MODE_INVALID }
```

相关声明：[max2221x_vdr_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gafced3b909c7963f0711bb23eecb4b538)、[MAX2221X_VDR_MODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggafced3b909c7963f0711bb23eecb4b538afe372c1bf8c9c3393600ffe8edaaf103)、[MAX2221X_VDR_MODE_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggafced3b909c7963f0711bb23eecb4b538a0eb8adae84e34d4bec22326d14ecfabc)、[MAX2221X_VDR_MODE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggafced3b909c7963f0711bb23eecb4b538a4d90473664901f26df9f23dea49ddc81)。

VDR 模式选项（VDR Mode Options）。

<a id="r_ga37baf31388784ee8bcd4204a9520b60c"></a>

```c
enum max2221x_vm_threshold { MAX2221X_VM_THRESHOLD_DISABLED = 0 , MAX2221X_VM_THRESHOLD_4500MV , MAX2221X_VM_THRESHOLD_6500MV , MAX2221X_VM_THRESHOLD_8500MV , MAX2221X_VM_THRESHOLD_10500MV , MAX2221X_VM_THRESHOLD_12500MV , MAX2221X_VM_THRESHOLD_14500MV , MAX2221X_VM_THRESHOLD_16500MV , MAX2221X_VM_THRESHOLD_18500MV , MAX2221X_VM_THRESHOLD_20500MV , MAX2221X_VM_THRESHOLD_22500MV , MAX2221X_VM_THRESHOLD_24500MV , MAX2221X_VM_THRESHOLD_26500MV , MAX2221X_VM_THRESHOLD_28500MV , MAX2221X_VM_THRESHOLD_30500MV , MAX2221X_VM_THRESHOLD_32500MV , MAX2221X_VM_THRESHOLD_INVALID }
```

相关声明：[max2221x_vm_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga37baf31388784ee8bcd4204a9520b60c)、[MAX2221X_VM_THRESHOLD_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cab2f1292ea8d5a4f57c7a267b7a5996b2)、[MAX2221X_VM_THRESHOLD_4500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cae739f6bd1a1d4278a307ea35a0403f89)、[MAX2221X_VM_THRESHOLD_6500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60caa46a4fc4d6a929fbd18010a0720f3e34)、[MAX2221X_VM_THRESHOLD_8500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca3b338a5c0c21c80dddbd8570ac39dd61)、[MAX2221X_VM_THRESHOLD_10500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca5790f7d7a22db4e5f4fb492dbe22eb44)、[MAX2221X_VM_THRESHOLD_12500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60caa8a63f696dfa28dd109a44575b51d0e0)、[MAX2221X_VM_THRESHOLD_14500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cab436636ab3fb6951d8c1ca638ac75dde)、[MAX2221X_VM_THRESHOLD_16500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca45d90c8af1a44579e7cf4024f3d9087d)、[MAX2221X_VM_THRESHOLD_18500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca148f57dd21fc83bf5db7786fff3ab1d7)、[MAX2221X_VM_THRESHOLD_20500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cad194e370f95f67ec36eb973803594422)、[MAX2221X_VM_THRESHOLD_22500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cad893cf892f7349e680b856f9c7bf7384)、[MAX2221X_VM_THRESHOLD_24500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cafe7b5948cfc315eadfd2402bac9ae6a6)、[MAX2221X_VM_THRESHOLD_26500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cafb77d719424231f9f7922de11754275c)、[MAX2221X_VM_THRESHOLD_28500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca2a88759e3ac3ef2e85552999df0589ae)、[MAX2221X_VM_THRESHOLD_30500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca492f5094e83bbb087de941a27801643f)、[MAX2221X_VM_THRESHOLD_32500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cafc7a32ab0f21bf055a6ae3c4f7946d0c)、[MAX2221X_VM_THRESHOLD_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca89fd9b164a9fad51545dbce7bb4fc3f8)。

VM 阈值电压等级（VM Threshold Voltage Levels）。

<a id="r_gaef62d32791c1393a527bb26f7a42173f"></a>

```c
enum max2221x_ctrl_mode { MAX2221X_CTRL_MODE_VOLT = 0 , MAX2221X_CTRL_MODE_CDR , MAX2221X_CTRL_MODE_LIMITER_VOLT , MAX2221X_CTRL_MODE_VOLT_CDR , MAX2221X_CTRL_MODE_INVALID }
```

相关声明：[max2221x_ctrl_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaef62d32791c1393a527bb26f7a42173f)、[MAX2221X_CTRL_MODE_VOLT](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173fa372f7920212b45635bb3ab73e524d3b6)、[MAX2221X_CTRL_MODE_CDR](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173faf006eb6ec53799777f20141e4b18ae65)、[MAX2221X_CTRL_MODE_LIMITER_VOLT](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173fa3df216e71e2e032db275a892de63de7c)、[MAX2221X_CTRL_MODE_VOLT_CDR](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173fa7ff1ba3a5cb0eba7d36cf3aacd1f3f36)、[MAX2221X_CTRL_MODE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173fa58053f83bdfef9587b04e9f122b28e76)。

控制模式选项（Control Mode Options）。

<a id="r_ga2e92402dac3bd8036d0f1eff3e546c62"></a>

```c
enum max2221x_ch_freq_div { MAX2221X_CH_FREQ_DIV_1 = 0 , MAX2221X_CH_FREQ_DIV_2 , MAX2221X_CH_FREQ_DIV_4 , MAX2221X_CH_FREQ_DIV_8 , MAX2221X_CH_FREQ_DIV_INVALID }
```

相关声明：[max2221x_ch_freq_div](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga2e92402dac3bd8036d0f1eff3e546c62)、[MAX2221X_CH_FREQ_DIV_1](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62ac69bf198154fd6084bdc981e1337b063)、[MAX2221X_CH_FREQ_DIV_2](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62ae8d46ab082eaf0ffea37eba0af34644e)、[MAX2221X_CH_FREQ_DIV_4](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62aed3e437b171469464e72ff0b3b28b7a9)、[MAX2221X_CH_FREQ_DIV_8](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62a85d1c13f410bc24356f8e93bd31c7f5e)、[MAX2221X_CH_FREQ_DIV_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62af01c9a7f7826740ebc76db2d091c476f)。

通道频率分频系数选项（Channel Frequency Divisor Options）。

<a id="r_gac3d8284e33a2cbc88e6e08396f6a2a66"></a>

```c
enum max2221x_slew_rate { MAX2221X_SLEW_RATE_FAST = 0 , MAX2221X_SLEW_RATE_400V_PER_US , MAX2221X_SLEW_RATE_200V_PER_US , MAX2221X_SLEW_RATE_100V_PER_US , MAX2221X_SLEW_RATE_INVALID }
```

相关声明：[max2221x_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gac3d8284e33a2cbc88e6e08396f6a2a66)、[MAX2221X_SLEW_RATE_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66a18b08f934c4c9923addad9e55ab9be5d)、[MAX2221X_SLEW_RATE_400V_PER_US](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66a6daf654eb4baaa6a59215fef63913a29)、[MAX2221X_SLEW_RATE_200V_PER_US](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66ad5a2520754e00735b2985c7627075e55)、[MAX2221X_SLEW_RATE_100V_PER_US](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66aa488670f38c32f36f37faf5421ab475b)、[MAX2221X_SLEW_RATE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66afe236cb49bf00f23d386d36f0c8ea600)。

压摆率选项（Slew Rate Options）。

<a id="r_ga064959a318df5a214758a95bc11ae8ed"></a>

```c
enum max2221x_gain { MAX2221X_SCALE_1 = 0 , MAX2221X_SCALE_2 , MAX2221X_SCALE_3 , MAX2221X_SCALE_4 , MAX2221X_GAIN_INVALID }
```

相关声明：[max2221x_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga064959a318df5a214758a95bc11ae8ed)、[MAX2221X_SCALE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8eda5727a7f4e76cb429be734014a48790c8)、[MAX2221X_SCALE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8eda90b7f2ecaf5c15746dea522d68da29c5)、[MAX2221X_SCALE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8eda8d370b6484c4e6ed5ff0533175fa0db1)、[MAX2221X_SCALE_4](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8eda3e5bf24a80ff6901a1de5946c79eb169)、[MAX2221X_GAIN_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8edacadcdeeb9fccb6e7ad947824cb68fe91)。

增益缩放选项（Gain Scale Options）。

<a id="r_ga5992183c2872bcf60726fb32784099c8"></a>

```c
enum max2221x_snsf { MAX2221X_SNSF_FULL_SCALE = 0 , MAX2221X_SNSF_2_3 , MAX2221X_SNSF_1_3 , MAX2221X_SNSF_INVALID }
```

相关声明：[max2221x_snsf](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5992183c2872bcf60726fb32784099c8)、[MAX2221X_SNSF_FULL_SCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga5992183c2872bcf60726fb32784099c8a4028f111fbb042857cda1c38c07ea773)、[MAX2221X_SNSF_2_3](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga5992183c2872bcf60726fb32784099c8a0cc4a45f17522eb715f9a515af2edd76)、[MAX2221X_SNSF_1_3](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga5992183c2872bcf60726fb32784099c8aeabf1fd560e09cd18cd3279248dd81ee)、[MAX2221X_SNSF_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga5992183c2872bcf60726fb32784099c8a4c9960e70786dd5945ffb1f4d7b18b44)。

检测滤波器选项（Sense Filter Options）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_ga5794ef47813b578767bf8d22c817bfc5"></a>

```c
int max2221x_set_master_chop_freq (const struct device *dev, enum max2221x_master_chop_freq freq)
```

相关声明：[max2221x_set_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5794ef47813b578767bf8d22c817bfc5)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga8f702fe056959c707d495a5b49ec7647)。

设置 MAX2221X 设备的主斩波频率（Master Chopping Frequency）。

<a id="r_gad283a38e9b32e9e721163feb2a7dc036"></a>

```c
int max2221x_get_master_chop_freq (const struct device *dev)
```

相关声明：[max2221x_get_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gad283a38e9b32e9e721163feb2a7dc036)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAX2221X 设备的主斩波频率（Master Chop Frequency）。

<a id="r_ga901b52fb1532c16cec31dc057085fb36"></a>

```c
int max2221x_get_channel_freq (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_channel_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga901b52fb1532c16cec31dc057085fb36)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备的通道频率（Channel Frequency）。

<a id="r_ga7eb45420e87a9dcb9642687208255d76"></a>

```c
int max2221x_set_part_state (const struct device *dev, bool enable)
```

相关声明：[max2221x_set_part_state](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga7eb45420e87a9dcb9642687208255d76)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 MAX2221X 设备的器件状态（Part State），即启用或禁用。

<a id="r_ga50da67dab16f368b83125cb6ffcdf173"></a>

```c
int max2221x_set_channel_state (const struct device *dev, uint8_t channel, bool enable)
```

相关声明：[max2221x_set_channel_state](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga50da67dab16f368b83125cb6ffcdf173)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 MAX2221X 设备某个通道的通道状态（Channel State），即启用或禁用。

<a id="r_gaa1ed035adbbe144a7637a86011d9e88c"></a>

```c
int max2221x_mask_fault_pin (const struct device *dev, enum max2221x_fault_pin_masks mask)
```

相关声明：[max2221x_mask_fault_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaa1ed035adbbe144a7637a86011d9e88c)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_fault_pin_masks](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga399738e28a4b7c309137d674e433ccb6)。

屏蔽 MAX2221X 设备对某种故障条件（Fault Condition）的检测。

<a id="r_ga44a628faff5a7bdd9117a272db2bf76b"></a>

```c
int max2221x_unmask_fault_pin (const struct device *dev, enum max2221x_fault_pin_masks mask)
```

相关声明：[max2221x_unmask_fault_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga44a628faff5a7bdd9117a272db2bf76b)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_fault_pin_masks](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga399738e28a4b7c309137d674e433ccb6)。

取消屏蔽 MAX2221X 设备对某种故障条件（Fault Condition）的检测。

<a id="r_ga0de71917ab9598525fce343c2b451edf"></a>

```c
int max2221x_set_vdr_mode (const struct device *dev, enum max2221x_vdr_mode mode)
```

相关声明：[max2221x_set_vdr_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga0de71917ab9598525fce343c2b451edf)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_vdr_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gafced3b909c7963f0711bb23eecb4b538)。

设置 MAX2221X 设备的 VDR 模式（VDR Mode）。

<a id="r_ga53d4b2faaee0b83b08729619dd42187d"></a>

```c
int max2221x_get_vdr_mode (const struct device *dev)
```

相关声明：[max2221x_get_vdr_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga53d4b2faaee0b83b08729619dd42187d)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAX2221X 设备的 VDR 模式（VDR Mode）。

<a id="r_ga239238ccddb28147365069850333701e"></a>

```c
int max2221x_read_status (const struct device *dev, uint16_t *status)
```

相关声明：[max2221x_read_status](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga239238ccddb28147365069850333701e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 MAX2221X 设备的状态（Status）。

<a id="r_ga0bd0b33a3020ccf22e726c38cf41dfd2"></a>

```c
int max2221x_read_vm_monitor (const struct device *dev, uint16_t *vm_monitor)
```

相关声明：[max2221x_read_vm_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga0bd0b33a3020ccf22e726c38cf41dfd2)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 MAX2221X 设备的电压监测器（Voltage Monitor）。

<a id="r_ga420b8f7c31431a9f44655301e348993e"></a>

```c
int max2221x_set_dc_h2l (const struct device *dev, uint16_t dc_hdl)
```

相关声明：[max2221x_set_dc_h2l](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga420b8f7c31431a9f44655301e348993e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 MAX2221X 设备的退磁电压（Demagnetization Voltage）。

<a id="r_gab7183c6bfa2c4ebf738f78d7a241d51e"></a>

```c
int max2221x_get_dc_h2l (const struct device *dev, uint16_t *dc_hdl)
```

相关声明：[max2221x_get_dc_h2l](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gab7183c6bfa2c4ebf738f78d7a241d51e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 MAX2221X 设备的退磁电压（Demagnetization Voltage）。

<a id="r_ga739a217f8e2e3518ca7223a05ea27f71"></a>

```c
int max2221x_set_vm_upper_threshold (const struct device *dev, enum max2221x_vm_threshold threshold)
```

相关声明：[max2221x_set_vm_upper_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga739a217f8e2e3518ca7223a05ea27f71)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_vm_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga37baf31388784ee8bcd4204a9520b60c)。

设置 MAX2221X 设备供电电压监测器的上阈值（Supply Voltage Monitor Upper Threshold）。

<a id="r_gac4d790ac301b3d2f0f17973ee631ce9a"></a>

```c
int max2221x_get_vm_upper_threshold (const struct device *dev)
```

相关声明：[max2221x_get_vm_upper_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gac4d790ac301b3d2f0f17973ee631ce9a)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAX2221X 设备供电电压监测器的上阈值（Supply Voltage Monitor Upper Threshold）。

<a id="r_ga8d417bccd2b1f015c8b985d0f8e64a41"></a>

```c
int max2221x_set_vm_lower_threshold (const struct device *dev, enum max2221x_vm_threshold threshold)
```

相关声明：[max2221x_set_vm_lower_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga8d417bccd2b1f015c8b985d0f8e64a41)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_vm_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga37baf31388784ee8bcd4204a9520b60c)。

设置 MAX2221X 设备供电电压监测器的下阈值（Supply Voltage Monitor Lower Threshold）。

<a id="r_gad3b27b5c1c43b05c4a80f1e3e9f9e4d3"></a>

```c
int max2221x_get_vm_lower_threshold (const struct device *dev)
```

相关声明：[max2221x_get_vm_lower_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gad3b27b5c1c43b05c4a80f1e3e9f9e4d3)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAX2221X 设备供电电压监测器的下阈值（Supply Voltage Monitor Lower Threshold）。

<a id="r_ga2d7680a00b951abb41cdf675c7d8346f"></a>

```c
int max2221x_read_dc_l2h (const struct device *dev, uint16_t *dc_l2h, uint8_t channel)
```

相关声明：[max2221x_read_dc_l2h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga2d7680a00b951abb41cdf675c7d8346f)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 MAX2221X 设备某个通道的 `DC_L2H` 值。

<a id="r_ga8075ed8e12d52083db84ba6f8756adb9"></a>

```c
int max2221x_write_dc_l2h (const struct device *dev, uint16_t dc_l2h, uint8_t channel)
```

相关声明：[max2221x_write_dc_l2h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga8075ed8e12d52083db84ba6f8756adb9)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 MAX2221X 设备某个通道的 `DC_L2H` 值。

<a id="r_gabf7cff9f7007a8a68d4b325beb4aa91a"></a>

```c
int max2221x_read_dc_h (const struct device *dev, uint16_t *dc_h, uint8_t channel)
```

相关声明：[max2221x_read_dc_h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gabf7cff9f7007a8a68d4b325beb4aa91a)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 MAX2221X 设备某个通道的 `DC_H` 值。

<a id="r_gaf60031b728ef83a515b6636c309b22d4"></a>

```c
int max2221x_write_dc_h (const struct device *dev, uint16_t dc_h, uint8_t channel)
```

相关声明：[max2221x_write_dc_h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaf60031b728ef83a515b6636c309b22d4)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 MAX2221X 设备某个通道的 `DC_H` 值。

<a id="r_ga59f7c6e2f29293dc0c7583b0375bab6f"></a>

```c
int max2221x_read_dc_l (const struct device *dev, uint16_t *dc_l, uint8_t channel)
```

相关声明：[max2221x_read_dc_l](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga59f7c6e2f29293dc0c7583b0375bab6f)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 MAX2221X 设备某个通道的 `DC_L` 值。

<a id="r_ga529818caa433e8b089f8d7948684ea93"></a>

```c
int max2221x_write_dc_l (const struct device *dev, uint16_t dc_l, uint8_t channel)
```

相关声明：[max2221x_write_dc_l](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga529818caa433e8b089f8d7948684ea93)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 MAX2221X 设备某个通道的 `DC_L` 值。

<a id="r_ga65acdb4bb13a934ed399c353e9c3501b"></a>

```c
int max2221x_read_time_l2h (const struct device *dev, uint16_t *time_l2h, uint8_t channel)
```

相关声明：[max2221x_read_time_l2h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga65acdb4bb13a934ed399c353e9c3501b)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 MAX2221X 设备某个通道的 L2H 时间值（Time L2H）。

<a id="r_ga5583299893b1e824ebac01447a6edb8d"></a>

```c
int max2221x_write_time_l2h (const struct device *dev, uint16_t time_l2h, uint8_t channel)
```

相关声明：[max2221x_write_time_l2h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5583299893b1e824ebac01447a6edb8d)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 MAX2221X 设备某个通道的 L2H 时间值（Time L2H）。

<a id="r_ga5a68165e4f5fbb0e6934572cd881889a"></a>

```c
int max2221x_set_ctrl_mode (const struct device *dev, enum max2221x_ctrl_mode mode, uint8_t channel)
```

相关声明：[max2221x_set_ctrl_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5a68165e4f5fbb0e6934572cd881889a)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_ctrl_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaef62d32791c1393a527bb26f7a42173f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 MAX2221X 设备某个通道的控制模式（Control Mode）。

<a id="r_ga5ad18cc556e62e132e878455c4cf5a4c"></a>

```c
int max2221x_get_ctrl_mode (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_ctrl_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5ad18cc556e62e132e878455c4cf5a4c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的控制模式（Control Mode）。

<a id="r_ga0cc46ca9e0437199b9a6685220c71ac1"></a>

```c
int max2221x_set_ramps (const struct device *dev, uint8_t channel, uint8_t ramp_mask, bool enable)
```

相关声明：[max2221x_set_ramps](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga0cc46ca9e0437199b9a6685220c71ac1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 MAX2221X 设备某个通道的斜坡（Ramps）。

<a id="r_ga9594a02a5cbf929acd982b7b93a5d4f8"></a>

```c
int max2221x_set_ramp_slew_rate (const struct device *dev, uint8_t channel, uint8_t ramp_slew_rate)
```

相关声明：[max2221x_set_ramp_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga9594a02a5cbf929acd982b7b93a5d4f8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 MAX2221X 设备某个通道的斜坡变化速率（Ramp Slew Rate）。

<a id="r_ga460a8a4be932da15268029c4785a022d"></a>

```c
int max2221x_get_ramp_slew_rate (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_ramp_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga460a8a4be932da15268029c4785a022d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的斜坡变化速率（Ramp Slew Rate）。

<a id="r_gaf3669424679108bafd9cf6ec9fdff1d1"></a>

```c
int max2221x_set_channel_chop_freq_div (const struct device *dev, uint8_t channel, enum max2221x_ch_freq_div freq_div)
```

相关声明：[max2221x_set_channel_chop_freq_div](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaf3669424679108bafd9cf6ec9fdff1d1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max2221x_ch_freq_div](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga2e92402dac3bd8036d0f1eff3e546c62)。

设置 MAX2221X 设备某个通道的斩波频率分频系数（Chopping Frequency Divider）。

<a id="r_gac1cd8396c8b72a60083727cc8ce6c79f"></a>

```c
int max2221x_get_channel_chop_freq_div (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_channel_chop_freq_div](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gac1cd8396c8b72a60083727cc8ce6c79f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的斩波频率分频系数（Chopping Frequency Divider）。

<a id="r_gab671df1d71393c7a83772aa90d525c38"></a>

```c
int max2221x_set_slew_rate (const struct device *dev, uint8_t channel, enum max2221x_slew_rate slew_rate)
```

相关声明：[max2221x_set_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gab671df1d71393c7a83772aa90d525c38)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max2221x_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gac3d8284e33a2cbc88e6e08396f6a2a66)。

设置 MAX2221X 设备某个通道的压摆率（Slew Rate）。

<a id="r_ga573d3cfca5ba3267a36c5817996d4f46"></a>

```c
int max2221x_get_slew_rate (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga573d3cfca5ba3267a36c5817996d4f46)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的压摆率（Slew Rate）。

<a id="r_ga2a553f33ccbea8780cd5aa6e8259b14d"></a>

```c
int max2221x_set_gain (const struct device *dev, uint8_t channel, enum max2221x_gain gain)
```

相关声明：[max2221x_set_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga2a553f33ccbea8780cd5aa6e8259b14d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max2221x_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga064959a318df5a214758a95bc11ae8ed)。

设置 MAX2221X 设备某个通道 CDR 的数字增益（Digital Gain）。

<a id="r_gaa76a1ff0edc8b403850d687b67006529"></a>

```c
int max2221x_get_gain (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaa76a1ff0edc8b403850d687b67006529)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道 CDR 的数字增益（Digital Gain）。

<a id="r_ga4c7ad2ac6af19be09ac4efef35fc9c60"></a>

```c
int max2221x_set_snsf (const struct device *dev, uint8_t channel, enum max2221x_snsf snsf)
```

相关声明：[max2221x_set_snsf](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga4c7ad2ac6af19be09ac4efef35fc9c60)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max2221x_snsf](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5992183c2872bcf60726fb32784099c8)。

设置 MAX2221X 设备某个通道的检测缩放系数（Sense Scaling Factor）。

<a id="r_ga441315200d66d8a798e76c59541573e9"></a>

```c
int max2221x_get_snsf (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_snsf](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga441315200d66d8a798e76c59541573e9)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的检测缩放系数（Sense Scaling Factor）。

<a id="r_ga6a3c9546787e80fb421ff57c1aafd24a"></a>

```c
int max2221x_read_pwm_dutycycle (const struct device *dev, uint8_t channel, uint16_t *duty_cycle)
```

相关声明：[max2221x_read_pwm_dutycycle](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga6a3c9546787e80fb421ff57c1aafd24a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 MAX2221X 设备某个通道的 PWM 占空比（Duty Cycle）。

<a id="r_ga5cc590f6f648ba1ff8cb96b369c1ea08"></a>

```c
int max2221x_read_fault0 (const struct device *dev)
```

相关声明：[max2221x_read_fault0](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5cc590f6f648ba1ff8cb96b369c1ea08)、[device](../device_reference/P002_设备对象结构.md)。

从 MAX2221X 设备的 `FAULT0` 寄存器读取故障状态（Fault Status）。

<a id="r_ga10fd9d6523ae83bb469076763f106fc1"></a>

```c
int max2221x_read_fault1 (const struct device *dev)
```

相关声明：[max2221x_read_fault1](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga10fd9d6523ae83bb469076763f106fc1)、[device](../device_reference/P002_设备对象结构.md)。

从 MAX2221X 设备的 `FAULT1` 寄存器读取故障状态（Fault Status）。

<a id="r_ga6255d9e0310281eccfacad971987a327"></a>

```c
int max2221x_set_on_time (const struct device *dev, uint8_t channel, uint16_t on_time_us)
```

相关声明：[max2221x_set_on_time](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga6255d9e0310281eccfacad971987a327)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 MAX2221X 设备某个通道的导通时间（On Time）。

<a id="r_ga685d70f78696d370acf9b0793121b24f"></a>

```c
int max2221x_get_on_time (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_on_time](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga685d70f78696d370acf9b0793121b24f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的导通时间（On Time）。

<a id="r_ga8e767d8da3317ca745c956a3758e4f1b"></a>

```c
int max2221x_set_off_time (const struct device *dev, uint8_t channel, uint16_t off_time_us)
```

相关声明：[max2221x_set_off_time](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga8e767d8da3317ca745c956a3758e4f1b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 MAX2221X 设备某个通道的关断时间（Off Time）。

<a id="r_ga7c78fbdcb856d34abbf061d292b4bebb"></a>

```c
int max2221x_get_off_time (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_off_time](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga7c78fbdcb856d34abbf061d292b4bebb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的关断时间（Off Time）。

<a id="r_gaaed34f21363e832ff1db043a990c4c31"></a>

```c
int max2221x_set_stop_state (const struct device *dev, uint8_t channel, bool stop_state)
```

相关声明：[max2221x_set_stop_state](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaaed34f21363e832ff1db043a990c4c31)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 MAX2221X 设备某个通道的停止状态（Stop State）。

<a id="r_gaafbc14d8bbdb5764e42b6e6ed5594122"></a>

```c
int max2221x_get_stop_state (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_stop_state](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaafbc14d8bbdb5764e42b6e6ed5594122)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的停止状态（Stop State）。

<a id="r_gae0c2320ed0790377ad1b3390a060db49"></a>

```c
int max2221x_set_repetitions (const struct device *dev, uint8_t channel, uint16_t repetitions)
```

相关声明：[max2221x_set_repetitions](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gae0c2320ed0790377ad1b3390a060db49)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 MAX2221X 设备某个通道的重复次数（Repetitions）。

<a id="r_ga94eb711a8039d9eacfc254bf26ddcf39"></a>

```c
int max2221x_get_repetitions (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_repetitions](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga94eb711a8039d9eacfc254bf26ddcf39)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的重复次数（Repetitions）。

<a id="r_gaa8a88aebc1d8c5d8290514b540574c28"></a>

```c
int max2221x_start_rapid_fire (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_start_rapid_fire](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaa8a88aebc1d8c5d8290514b540574c28)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启动 MAX2221X 设备某个通道的快速连续触发模式（Rapid Fire Mode）。

<a id="r_ga6dc255318516cff52662d7c5533a0f74"></a>

```c
int max2221x_stop_rapid_fire (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_stop_rapid_fire](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga6dc255318516cff52662d7c5533a0f74)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

停止 MAX2221X 设备某个通道的快速连续触发模式（Rapid Fire Mode）。


## 7.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P532_max2221x.h_源码浏览.md)
- [MAX2221X_RAMP_DOWN_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gae933f32f8cf7328dca2afb7f344dcb29)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [MAX2221X_RAMP_MID_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gacb47da8940b93285c56693dee2aca071)
- [MAX2221X_RAMP_UP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga73042e2ff448d10d2b36135f1f2fd27e)
- [max2221x_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga8f702fe056959c707d495a5b49ec7647)
- [MAX2221X_FREQ_100KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab689b993d9fa98c5bf140162723d2feb)
- [MAX2221X_FREQ_80KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1a478348731bd456313912f6b4a59f1f)
- [MAX2221X_FREQ_60KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a93bf099ae22e26de9885c76bc8428eb8)
- [MAX2221X_FREQ_50KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1710af28d11faf44c423f2f771f02980)
- [MAX2221X_FREQ_40KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a34a90a18c91e8e6f547c0788d4061612)
- [MAX2221X_FREQ_30KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab4e2229b6516ea4f7278fa2931f262ed)
- [MAX2221X_FREQ_25KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a8a11aacff6d925230f8719508b432cef)
- [MAX2221X_FREQ_20KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a5cdbdb4c266cca9ae859f20dc0187a15)
- [MAX2221X_FREQ_15KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647aa39e41621ac0f7f7073d95cfa18c99a4)
- [MAX2221X_FREQ_10KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647abcaa72d42d74f8054480c73bf3fa61f5)
- [MAX2221X_FREQ_7500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a208bff3bc2c214ea84404ba49c1037cb)
- [MAX2221X_FREQ_5000HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a0e56c34ed02843a63bbcfe0d219b2dbc)
- [MAX2221X_FREQ_2500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a30dbf5e8aa5f7aa61cff6cf7391e39c9)
- [MAX2221X_FREQ_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a2bfeae761213ed84221a6bda013599aa)
- [max2221x_individual_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga41010c75c9cb6ed23e06cfec0ebbe413)
- [MAX2221X_FREQ_M](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a4cee57aef5be5d79919513fea3891490)
- [MAX2221X_FREQ_M_2](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a120c21fdf16a48795233bae403a0c3f1)
- [MAX2221X_FREQ_M_4](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a84119a5bb314c03760637ebb05a7f16a)
- [MAX2221X_FREQ_M_8](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413ac0955ebf50e1c3d7a51e6aa42e008cfd)
- [MAX2221X_FREQ_M_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413af6f9cae164f70b5fc9a7003e526d15b2)
- [max2221x_fault_pin_masks](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga399738e28a4b7c309137d674e433ccb6)
- [MAX2221X_FAULT_PIN_UVM](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a9cf6ad6bb71092f7e28eb7de91e92a51)
- [MAX2221X_FAULT_PIN_COMF](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a9492bcaf6e4e5e41bca5d156b7cbde92)
- [MAX2221X_FAULT_PIN_DPM](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a12806ad411905619c15ed7cc603cdb36)
- [MAX2221X_FAULT_PIN_HHF](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a28bb4d3f65348762116f5a14b6a4614f)
- [MAX2221X_FAULT_PIN_OLF](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a5dcb7a29041c5ec4b399795cf59db322)
- [MAX2221X_FAULT_PIN_OCP](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6aae654309f343b46f117327afe025c789)
- [MAX2221X_FAULT_PIN_OVT](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a1f2abcecc1b2ad5092322034797fa391)
- [MAX2221X_FAULT_PIN_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga399738e28a4b7c309137d674e433ccb6a41a39797fc9dfc70c31f7fa08d083354)
- [max2221x_vdr_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gafced3b909c7963f0711bb23eecb4b538)
- [MAX2221X_VDR_MODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggafced3b909c7963f0711bb23eecb4b538afe372c1bf8c9c3393600ffe8edaaf103)
- [MAX2221X_VDR_MODE_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggafced3b909c7963f0711bb23eecb4b538a0eb8adae84e34d4bec22326d14ecfabc)
- [MAX2221X_VDR_MODE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggafced3b909c7963f0711bb23eecb4b538a4d90473664901f26df9f23dea49ddc81)
- [max2221x_vm_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga37baf31388784ee8bcd4204a9520b60c)
- [MAX2221X_VM_THRESHOLD_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cab2f1292ea8d5a4f57c7a267b7a5996b2)
- [MAX2221X_VM_THRESHOLD_4500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cae739f6bd1a1d4278a307ea35a0403f89)
- [MAX2221X_VM_THRESHOLD_6500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60caa46a4fc4d6a929fbd18010a0720f3e34)
- [MAX2221X_VM_THRESHOLD_8500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca3b338a5c0c21c80dddbd8570ac39dd61)
- [MAX2221X_VM_THRESHOLD_10500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca5790f7d7a22db4e5f4fb492dbe22eb44)
- [MAX2221X_VM_THRESHOLD_12500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60caa8a63f696dfa28dd109a44575b51d0e0)
- [MAX2221X_VM_THRESHOLD_14500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cab436636ab3fb6951d8c1ca638ac75dde)
- [MAX2221X_VM_THRESHOLD_16500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca45d90c8af1a44579e7cf4024f3d9087d)
- [MAX2221X_VM_THRESHOLD_18500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca148f57dd21fc83bf5db7786fff3ab1d7)
- [MAX2221X_VM_THRESHOLD_20500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cad194e370f95f67ec36eb973803594422)
- [MAX2221X_VM_THRESHOLD_22500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cad893cf892f7349e680b856f9c7bf7384)
- [MAX2221X_VM_THRESHOLD_24500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cafe7b5948cfc315eadfd2402bac9ae6a6)
- [MAX2221X_VM_THRESHOLD_26500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cafb77d719424231f9f7922de11754275c)
- [MAX2221X_VM_THRESHOLD_28500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca2a88759e3ac3ef2e85552999df0589ae)
- [MAX2221X_VM_THRESHOLD_30500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca492f5094e83bbb087de941a27801643f)
- [MAX2221X_VM_THRESHOLD_32500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60cafc7a32ab0f21bf055a6ae3c4f7946d0c)
- [MAX2221X_VM_THRESHOLD_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga37baf31388784ee8bcd4204a9520b60ca89fd9b164a9fad51545dbce7bb4fc3f8)
- [max2221x_ctrl_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaef62d32791c1393a527bb26f7a42173f)
- [MAX2221X_CTRL_MODE_VOLT](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173fa372f7920212b45635bb3ab73e524d3b6)
- [MAX2221X_CTRL_MODE_CDR](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173faf006eb6ec53799777f20141e4b18ae65)
- [MAX2221X_CTRL_MODE_LIMITER_VOLT](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173fa3df216e71e2e032db275a892de63de7c)
- [MAX2221X_CTRL_MODE_VOLT_CDR](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173fa7ff1ba3a5cb0eba7d36cf3aacd1f3f36)
- [MAX2221X_CTRL_MODE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggaef62d32791c1393a527bb26f7a42173fa58053f83bdfef9587b04e9f122b28e76)
- [max2221x_ch_freq_div](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga2e92402dac3bd8036d0f1eff3e546c62)
- [MAX2221X_CH_FREQ_DIV_1](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62ac69bf198154fd6084bdc981e1337b063)
- [MAX2221X_CH_FREQ_DIV_2](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62ae8d46ab082eaf0ffea37eba0af34644e)
- [MAX2221X_CH_FREQ_DIV_4](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62aed3e437b171469464e72ff0b3b28b7a9)
- [MAX2221X_CH_FREQ_DIV_8](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62a85d1c13f410bc24356f8e93bd31c7f5e)
- [MAX2221X_CH_FREQ_DIV_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga2e92402dac3bd8036d0f1eff3e546c62af01c9a7f7826740ebc76db2d091c476f)
- [max2221x_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gac3d8284e33a2cbc88e6e08396f6a2a66)
- [MAX2221X_SLEW_RATE_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66a18b08f934c4c9923addad9e55ab9be5d)
- [MAX2221X_SLEW_RATE_400V_PER_US](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66a6daf654eb4baaa6a59215fef63913a29)
- [MAX2221X_SLEW_RATE_200V_PER_US](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66ad5a2520754e00735b2985c7627075e55)
- [MAX2221X_SLEW_RATE_100V_PER_US](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66aa488670f38c32f36f37faf5421ab475b)
- [MAX2221X_SLEW_RATE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ggac3d8284e33a2cbc88e6e08396f6a2a66afe236cb49bf00f23d386d36f0c8ea600)
- [max2221x_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga064959a318df5a214758a95bc11ae8ed)
- [MAX2221X_SCALE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8eda5727a7f4e76cb429be734014a48790c8)
- [MAX2221X_SCALE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8eda90b7f2ecaf5c15746dea522d68da29c5)
- [MAX2221X_SCALE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8eda8d370b6484c4e6ed5ff0533175fa0db1)
- [MAX2221X_SCALE_4](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8eda3e5bf24a80ff6901a1de5946c79eb169)
- [MAX2221X_GAIN_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga064959a318df5a214758a95bc11ae8edacadcdeeb9fccb6e7ad947824cb68fe91)
- [max2221x_snsf](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5992183c2872bcf60726fb32784099c8)
- [MAX2221X_SNSF_FULL_SCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga5992183c2872bcf60726fb32784099c8a4028f111fbb042857cda1c38c07ea773)
- [MAX2221X_SNSF_2_3](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga5992183c2872bcf60726fb32784099c8a0cc4a45f17522eb715f9a515af2edd76)
- [MAX2221X_SNSF_1_3](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga5992183c2872bcf60726fb32784099c8aeabf1fd560e09cd18cd3279248dd81ee)
- [MAX2221X_SNSF_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gga5992183c2872bcf60726fb32784099c8a4c9960e70786dd5945ffb1f4d7b18b44)
- [max2221x_set_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5794ef47813b578767bf8d22c817bfc5)
- [device](../device_reference/P002_设备对象结构.md)
- [max2221x_get_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gad283a38e9b32e9e721163feb2a7dc036)
- [max2221x_get_channel_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga901b52fb1532c16cec31dc057085fb36)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [max2221x_set_part_state](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga7eb45420e87a9dcb9642687208255d76)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [max2221x_set_channel_state](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga50da67dab16f368b83125cb6ffcdf173)
- [max2221x_mask_fault_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaa1ed035adbbe144a7637a86011d9e88c)
- [max2221x_unmask_fault_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga44a628faff5a7bdd9117a272db2bf76b)
- [max2221x_set_vdr_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga0de71917ab9598525fce343c2b451edf)
- [max2221x_get_vdr_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga53d4b2faaee0b83b08729619dd42187d)
- [max2221x_read_status](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga239238ccddb28147365069850333701e)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [max2221x_read_vm_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga0bd0b33a3020ccf22e726c38cf41dfd2)
- [max2221x_set_dc_h2l](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga420b8f7c31431a9f44655301e348993e)
- [max2221x_get_dc_h2l](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gab7183c6bfa2c4ebf738f78d7a241d51e)
- [max2221x_set_vm_upper_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga739a217f8e2e3518ca7223a05ea27f71)
- [max2221x_get_vm_upper_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gac4d790ac301b3d2f0f17973ee631ce9a)
- [max2221x_set_vm_lower_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga8d417bccd2b1f015c8b985d0f8e64a41)
- [max2221x_get_vm_lower_threshold](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gad3b27b5c1c43b05c4a80f1e3e9f9e4d3)
- [max2221x_read_dc_l2h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga2d7680a00b951abb41cdf675c7d8346f)
- [max2221x_write_dc_l2h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga8075ed8e12d52083db84ba6f8756adb9)
- [max2221x_read_dc_h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gabf7cff9f7007a8a68d4b325beb4aa91a)
- [max2221x_write_dc_h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaf60031b728ef83a515b6636c309b22d4)
- [max2221x_read_dc_l](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga59f7c6e2f29293dc0c7583b0375bab6f)
- [max2221x_write_dc_l](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga529818caa433e8b089f8d7948684ea93)
- [max2221x_read_time_l2h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga65acdb4bb13a934ed399c353e9c3501b)
- [max2221x_write_time_l2h](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5583299893b1e824ebac01447a6edb8d)
- [max2221x_set_ctrl_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5a68165e4f5fbb0e6934572cd881889a)
- [max2221x_get_ctrl_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5ad18cc556e62e132e878455c4cf5a4c)
- [max2221x_set_ramps](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga0cc46ca9e0437199b9a6685220c71ac1)
- [max2221x_set_ramp_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga9594a02a5cbf929acd982b7b93a5d4f8)
- [max2221x_get_ramp_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga460a8a4be932da15268029c4785a022d)
- [max2221x_set_channel_chop_freq_div](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaf3669424679108bafd9cf6ec9fdff1d1)
- [max2221x_get_channel_chop_freq_div](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gac1cd8396c8b72a60083727cc8ce6c79f)
- [max2221x_set_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gab671df1d71393c7a83772aa90d525c38)
- [max2221x_get_slew_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga573d3cfca5ba3267a36c5817996d4f46)
- [max2221x_set_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga2a553f33ccbea8780cd5aa6e8259b14d)
- [max2221x_get_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaa76a1ff0edc8b403850d687b67006529)
- [max2221x_set_snsf](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga4c7ad2ac6af19be09ac4efef35fc9c60)
- [max2221x_get_snsf](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga441315200d66d8a798e76c59541573e9)
- [max2221x_read_pwm_dutycycle](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga6a3c9546787e80fb421ff57c1aafd24a)
- [max2221x_read_fault0](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga5cc590f6f648ba1ff8cb96b369c1ea08)
- [max2221x_read_fault1](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga10fd9d6523ae83bb469076763f106fc1)
- [max2221x_set_on_time](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga6255d9e0310281eccfacad971987a327)
- [max2221x_get_on_time](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga685d70f78696d370acf9b0793121b24f)
- [max2221x_set_off_time](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga8e767d8da3317ca745c956a3758e4f1b)
- [max2221x_get_off_time](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga7c78fbdcb856d34abbf061d292b4bebb)
- [max2221x_set_stop_state](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaaed34f21363e832ff1db043a990c4c31)
- [max2221x_get_stop_state](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaafbc14d8bbdb5764e42b6e6ed5594122)
- [max2221x_set_repetitions](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gae0c2320ed0790377ad1b3390a060db49)
- [max2221x_get_repetitions](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga94eb711a8039d9eacfc254bf26ddcf39)
- [max2221x_start_rapid_fire](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#gaa8a88aebc1d8c5d8290514b540574c28)
- [max2221x_stop_rapid_fire](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html#ga6dc255318516cff52662d7c5533a0f74)

<a id="header-details"></a>

---

[上一章](P006_zephyr__audio__midi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__net__net_context.h_文件参考.md)
