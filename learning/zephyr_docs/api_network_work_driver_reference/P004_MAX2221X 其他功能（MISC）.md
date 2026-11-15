---
id: learning.zephyr-docs.api-network-work-driver-reference.page-4
title: MAX2221X 其他功能（MISC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_MAX2221X 其他功能（MISC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__max2221x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_max2221x_2Eh"></a>

```c
file max2221x.h
```

相关声明：[max2221x.h](../api_file_network_pcie_reference/P007_zephyr__drivers__misc__max2221x__max2221x.h_文件参考.md)。

MAX2221X杂项（MISC）驱动的公共API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.2\_枚举（Enumerations）

<a id="r_ga8f702fe056959c707d495a5b49ec7647"></a>

```c
enum max2221x_master_chop_freq { MAX2221X_FREQ_100KHZ = 0 , MAX2221X_FREQ_80KHZ , MAX2221X_FREQ_60KHZ , MAX2221X_FREQ_50KHZ , MAX2221X_FREQ_40KHZ , MAX2221X_FREQ_30KHZ , MAX2221X_FREQ_25KHZ , MAX2221X_FREQ_20KHZ , MAX2221X_FREQ_15KHZ , MAX2221X_FREQ_10KHZ , MAX2221X_FREQ_7500HZ , MAX2221X_FREQ_5000HZ , MAX2221X_FREQ_2500HZ , MAX2221X_FREQ_INVALID }
```

相关声明：[max2221x_master_chop_freq](#ga8f702fe056959c707d495a5b49ec7647)、[MAX2221X_FREQ_100KHZ](#gga8f702fe056959c707d495a5b49ec7647ab689b993d9fa98c5bf140162723d2feb)、[MAX2221X_FREQ_80KHZ](#gga8f702fe056959c707d495a5b49ec7647a1a478348731bd456313912f6b4a59f1f)、[MAX2221X_FREQ_60KHZ](#gga8f702fe056959c707d495a5b49ec7647a93bf099ae22e26de9885c76bc8428eb8)、[MAX2221X_FREQ_50KHZ](#gga8f702fe056959c707d495a5b49ec7647a1710af28d11faf44c423f2f771f02980)、[MAX2221X_FREQ_40KHZ](#gga8f702fe056959c707d495a5b49ec7647a34a90a18c91e8e6f547c0788d4061612)、[MAX2221X_FREQ_30KHZ](#gga8f702fe056959c707d495a5b49ec7647ab4e2229b6516ea4f7278fa2931f262ed)、[MAX2221X_FREQ_25KHZ](#gga8f702fe056959c707d495a5b49ec7647a8a11aacff6d925230f8719508b432cef)、[MAX2221X_FREQ_20KHZ](#gga8f702fe056959c707d495a5b49ec7647a5cdbdb4c266cca9ae859f20dc0187a15)、[MAX2221X_FREQ_15KHZ](#gga8f702fe056959c707d495a5b49ec7647aa39e41621ac0f7f7073d95cfa18c99a4)、[MAX2221X_FREQ_10KHZ](#gga8f702fe056959c707d495a5b49ec7647abcaa72d42d74f8054480c73bf3fa61f5)、[MAX2221X_FREQ_7500HZ](#gga8f702fe056959c707d495a5b49ec7647a208bff3bc2c214ea84404ba49c1037cb)、[MAX2221X_FREQ_5000HZ](#gga8f702fe056959c707d495a5b49ec7647a0e56c34ed02843a63bbcfe0d219b2dbc)、[MAX2221X_FREQ_2500HZ](#gga8f702fe056959c707d495a5b49ec7647a30dbf5e8aa5f7aa61cff6cf7391e39c9)、[MAX2221X_FREQ_INVALID](#gga8f702fe056959c707d495a5b49ec7647a2bfeae761213ed84221a6bda013599aa)。

主斩波频率（Master Chopping Frequency）选项。

<a id="r_ga41010c75c9cb6ed23e06cfec0ebbe413"></a>

```c
enum max2221x_individual_chop_freq { MAX2221X_FREQ_M = 0 , MAX2221X_FREQ_M_2 , MAX2221X_FREQ_M_4 , MAX2221X_FREQ_M_8 , MAX2221X_FREQ_M_INVALID }
```

相关声明：[max2221x_individual_chop_freq](#ga41010c75c9cb6ed23e06cfec0ebbe413)、[MAX2221X_FREQ_M](#gga41010c75c9cb6ed23e06cfec0ebbe413a4cee57aef5be5d79919513fea3891490)、[MAX2221X_FREQ_M_2](#gga41010c75c9cb6ed23e06cfec0ebbe413a120c21fdf16a48795233bae403a0c3f1)、[MAX2221X_FREQ_M_4](#gga41010c75c9cb6ed23e06cfec0ebbe413a84119a5bb314c03760637ebb05a7f16a)、[MAX2221X_FREQ_M_8](#gga41010c75c9cb6ed23e06cfec0ebbe413ac0955ebf50e1c3d7a51e6aa42e008cfd)、[MAX2221X_FREQ_M_INVALID](#gga41010c75c9cb6ed23e06cfec0ebbe413af6f9cae164f70b5fc9a7003e526d15b2)。

独立通道斩波频率分频系数（Chopping Frequency Divisor）选项。

<a id="r_ga399738e28a4b7c309137d674e433ccb6"></a>

```c
enum max2221x_fault_pin_masks { MAX2221X_FAULT_PIN_UVM = 0 , MAX2221X_FAULT_PIN_COMF , MAX2221X_FAULT_PIN_DPM , MAX2221X_FAULT_PIN_HHF , MAX2221X_FAULT_PIN_OLF , MAX2221X_FAULT_PIN_OCP , MAX2221X_FAULT_PIN_OVT , MAX2221X_FAULT_PIN_INVALID }
```

相关声明：[max2221x_fault_pin_masks](#ga399738e28a4b7c309137d674e433ccb6)、[MAX2221X_FAULT_PIN_UVM](#gga399738e28a4b7c309137d674e433ccb6a9cf6ad6bb71092f7e28eb7de91e92a51)、[MAX2221X_FAULT_PIN_COMF](#gga399738e28a4b7c309137d674e433ccb6a9492bcaf6e4e5e41bca5d156b7cbde92)、[MAX2221X_FAULT_PIN_DPM](#gga399738e28a4b7c309137d674e433ccb6a12806ad411905619c15ed7cc603cdb36)、[MAX2221X_FAULT_PIN_HHF](#gga399738e28a4b7c309137d674e433ccb6a28bb4d3f65348762116f5a14b6a4614f)、[MAX2221X_FAULT_PIN_OLF](#gga399738e28a4b7c309137d674e433ccb6a5dcb7a29041c5ec4b399795cf59db322)、[MAX2221X_FAULT_PIN_OCP](#gga399738e28a4b7c309137d674e433ccb6aae654309f343b46f117327afe025c789)、[MAX2221X_FAULT_PIN_OVT](#gga399738e28a4b7c309137d674e433ccb6a1f2abcecc1b2ad5092322034797fa391)、[MAX2221X_FAULT_PIN_INVALID](#gga399738e28a4b7c309137d674e433ccb6a41a39797fc9dfc70c31f7fa08d083354)。

故障引脚掩码定义（Fault Pin Mask Definitions）。

<a id="r_gafced3b909c7963f0711bb23eecb4b538"></a>

```c
enum max2221x_vdr_mode { MAX2221X_VDR_MODE_NORMAL = 0 , MAX2221X_VDR_MODE_DUTY , MAX2221X_VDR_MODE_INVALID }
```

相关声明：[max2221x_vdr_mode](#gafced3b909c7963f0711bb23eecb4b538)、[MAX2221X_VDR_MODE_NORMAL](#ggafced3b909c7963f0711bb23eecb4b538afe372c1bf8c9c3393600ffe8edaaf103)、[MAX2221X_VDR_MODE_DUTY](#ggafced3b909c7963f0711bb23eecb4b538a0eb8adae84e34d4bec22326d14ecfabc)、[MAX2221X_VDR_MODE_INVALID](#ggafced3b909c7963f0711bb23eecb4b538a4d90473664901f26df9f23dea49ddc81)。

VDR 模式选项（VDR Mode Options）。

<a id="r_ga37baf31388784ee8bcd4204a9520b60c"></a>

```c
enum max2221x_vm_threshold { MAX2221X_VM_THRESHOLD_DISABLED = 0 , MAX2221X_VM_THRESHOLD_4500MV , MAX2221X_VM_THRESHOLD_6500MV , MAX2221X_VM_THRESHOLD_8500MV , MAX2221X_VM_THRESHOLD_10500MV , MAX2221X_VM_THRESHOLD_12500MV , MAX2221X_VM_THRESHOLD_14500MV , MAX2221X_VM_THRESHOLD_16500MV , MAX2221X_VM_THRESHOLD_18500MV , MAX2221X_VM_THRESHOLD_20500MV , MAX2221X_VM_THRESHOLD_22500MV , MAX2221X_VM_THRESHOLD_24500MV , MAX2221X_VM_THRESHOLD_26500MV , MAX2221X_VM_THRESHOLD_28500MV , MAX2221X_VM_THRESHOLD_30500MV , MAX2221X_VM_THRESHOLD_32500MV , MAX2221X_VM_THRESHOLD_INVALID }
```

相关声明：[max2221x_vm_threshold](#ga37baf31388784ee8bcd4204a9520b60c)、[MAX2221X_VM_THRESHOLD_DISABLED](#gga37baf31388784ee8bcd4204a9520b60cab2f1292ea8d5a4f57c7a267b7a5996b2)、[MAX2221X_VM_THRESHOLD_4500MV](#gga37baf31388784ee8bcd4204a9520b60cae739f6bd1a1d4278a307ea35a0403f89)、[MAX2221X_VM_THRESHOLD_6500MV](#gga37baf31388784ee8bcd4204a9520b60caa46a4fc4d6a929fbd18010a0720f3e34)、[MAX2221X_VM_THRESHOLD_8500MV](#gga37baf31388784ee8bcd4204a9520b60ca3b338a5c0c21c80dddbd8570ac39dd61)、[MAX2221X_VM_THRESHOLD_10500MV](#gga37baf31388784ee8bcd4204a9520b60ca5790f7d7a22db4e5f4fb492dbe22eb44)、[MAX2221X_VM_THRESHOLD_12500MV](#gga37baf31388784ee8bcd4204a9520b60caa8a63f696dfa28dd109a44575b51d0e0)、[MAX2221X_VM_THRESHOLD_14500MV](#gga37baf31388784ee8bcd4204a9520b60cab436636ab3fb6951d8c1ca638ac75dde)、[MAX2221X_VM_THRESHOLD_16500MV](#gga37baf31388784ee8bcd4204a9520b60ca45d90c8af1a44579e7cf4024f3d9087d)、[MAX2221X_VM_THRESHOLD_18500MV](#gga37baf31388784ee8bcd4204a9520b60ca148f57dd21fc83bf5db7786fff3ab1d7)、[MAX2221X_VM_THRESHOLD_20500MV](#gga37baf31388784ee8bcd4204a9520b60cad194e370f95f67ec36eb973803594422)、[MAX2221X_VM_THRESHOLD_22500MV](#gga37baf31388784ee8bcd4204a9520b60cad893cf892f7349e680b856f9c7bf7384)、[MAX2221X_VM_THRESHOLD_24500MV](#gga37baf31388784ee8bcd4204a9520b60cafe7b5948cfc315eadfd2402bac9ae6a6)、[MAX2221X_VM_THRESHOLD_26500MV](#gga37baf31388784ee8bcd4204a9520b60cafb77d719424231f9f7922de11754275c)、[MAX2221X_VM_THRESHOLD_28500MV](#gga37baf31388784ee8bcd4204a9520b60ca2a88759e3ac3ef2e85552999df0589ae)、[MAX2221X_VM_THRESHOLD_30500MV](#gga37baf31388784ee8bcd4204a9520b60ca492f5094e83bbb087de941a27801643f)、[MAX2221X_VM_THRESHOLD_32500MV](#gga37baf31388784ee8bcd4204a9520b60cafc7a32ab0f21bf055a6ae3c4f7946d0c)、[MAX2221X_VM_THRESHOLD_INVALID](#gga37baf31388784ee8bcd4204a9520b60ca89fd9b164a9fad51545dbce7bb4fc3f8)。

VM 阈值电压等级（VM Threshold Voltage Levels）。

<a id="r_gaef62d32791c1393a527bb26f7a42173f"></a>

```c
enum max2221x_ctrl_mode { MAX2221X_CTRL_MODE_VOLT = 0 , MAX2221X_CTRL_MODE_CDR , MAX2221X_CTRL_MODE_LIMITER_VOLT , MAX2221X_CTRL_MODE_VOLT_CDR , MAX2221X_CTRL_MODE_INVALID }
```

相关声明：[max2221x_ctrl_mode](#gaef62d32791c1393a527bb26f7a42173f)、[MAX2221X_CTRL_MODE_VOLT](#ggaef62d32791c1393a527bb26f7a42173fa372f7920212b45635bb3ab73e524d3b6)、[MAX2221X_CTRL_MODE_CDR](#ggaef62d32791c1393a527bb26f7a42173faf006eb6ec53799777f20141e4b18ae65)、[MAX2221X_CTRL_MODE_LIMITER_VOLT](#ggaef62d32791c1393a527bb26f7a42173fa3df216e71e2e032db275a892de63de7c)、[MAX2221X_CTRL_MODE_VOLT_CDR](#ggaef62d32791c1393a527bb26f7a42173fa7ff1ba3a5cb0eba7d36cf3aacd1f3f36)、[MAX2221X_CTRL_MODE_INVALID](#ggaef62d32791c1393a527bb26f7a42173fa58053f83bdfef9587b04e9f122b28e76)。

控制模式选项（Control Mode Options）。

<a id="r_ga2e92402dac3bd8036d0f1eff3e546c62"></a>

```c
enum max2221x_ch_freq_div { MAX2221X_CH_FREQ_DIV_1 = 0 , MAX2221X_CH_FREQ_DIV_2 , MAX2221X_CH_FREQ_DIV_4 , MAX2221X_CH_FREQ_DIV_8 , MAX2221X_CH_FREQ_DIV_INVALID }
```

相关声明：[max2221x_ch_freq_div](#ga2e92402dac3bd8036d0f1eff3e546c62)、[MAX2221X_CH_FREQ_DIV_1](#gga2e92402dac3bd8036d0f1eff3e546c62ac69bf198154fd6084bdc981e1337b063)、[MAX2221X_CH_FREQ_DIV_2](#gga2e92402dac3bd8036d0f1eff3e546c62ae8d46ab082eaf0ffea37eba0af34644e)、[MAX2221X_CH_FREQ_DIV_4](#gga2e92402dac3bd8036d0f1eff3e546c62aed3e437b171469464e72ff0b3b28b7a9)、[MAX2221X_CH_FREQ_DIV_8](#gga2e92402dac3bd8036d0f1eff3e546c62a85d1c13f410bc24356f8e93bd31c7f5e)、[MAX2221X_CH_FREQ_DIV_INVALID](#gga2e92402dac3bd8036d0f1eff3e546c62af01c9a7f7826740ebc76db2d091c476f)。

通道频率分频系数选项（Channel Frequency Divisor Options）。

<a id="r_gac3d8284e33a2cbc88e6e08396f6a2a66"></a>

```c
enum max2221x_slew_rate { MAX2221X_SLEW_RATE_FAST = 0 , MAX2221X_SLEW_RATE_400V_PER_US , MAX2221X_SLEW_RATE_200V_PER_US , MAX2221X_SLEW_RATE_100V_PER_US , MAX2221X_SLEW_RATE_INVALID }
```

相关声明：[max2221x_slew_rate](#gac3d8284e33a2cbc88e6e08396f6a2a66)、[MAX2221X_SLEW_RATE_FAST](#ggac3d8284e33a2cbc88e6e08396f6a2a66a18b08f934c4c9923addad9e55ab9be5d)、[MAX2221X_SLEW_RATE_400V_PER_US](#ggac3d8284e33a2cbc88e6e08396f6a2a66a6daf654eb4baaa6a59215fef63913a29)、[MAX2221X_SLEW_RATE_200V_PER_US](#ggac3d8284e33a2cbc88e6e08396f6a2a66ad5a2520754e00735b2985c7627075e55)、[MAX2221X_SLEW_RATE_100V_PER_US](#ggac3d8284e33a2cbc88e6e08396f6a2a66aa488670f38c32f36f37faf5421ab475b)、[MAX2221X_SLEW_RATE_INVALID](#ggac3d8284e33a2cbc88e6e08396f6a2a66afe236cb49bf00f23d386d36f0c8ea600)。

压摆率选项（Slew Rate Options）。

<a id="r_ga064959a318df5a214758a95bc11ae8ed"></a>

```c
enum max2221x_gain { MAX2221X_SCALE_1 = 0 , MAX2221X_SCALE_2 , MAX2221X_SCALE_3 , MAX2221X_SCALE_4 , MAX2221X_GAIN_INVALID }
```

相关声明：[max2221x_gain](#ga064959a318df5a214758a95bc11ae8ed)、[MAX2221X_SCALE_1](#gga064959a318df5a214758a95bc11ae8eda5727a7f4e76cb429be734014a48790c8)、[MAX2221X_SCALE_2](#gga064959a318df5a214758a95bc11ae8eda90b7f2ecaf5c15746dea522d68da29c5)、[MAX2221X_SCALE_3](#gga064959a318df5a214758a95bc11ae8eda8d370b6484c4e6ed5ff0533175fa0db1)、[MAX2221X_SCALE_4](#gga064959a318df5a214758a95bc11ae8eda3e5bf24a80ff6901a1de5946c79eb169)、[MAX2221X_GAIN_INVALID](#gga064959a318df5a214758a95bc11ae8edacadcdeeb9fccb6e7ad947824cb68fe91)。

增益缩放选项（Gain Scale Options）。

<a id="r_ga5992183c2872bcf60726fb32784099c8"></a>

```c
enum max2221x_snsf { MAX2221X_SNSF_FULL_SCALE = 0 , MAX2221X_SNSF_2_3 , MAX2221X_SNSF_1_3 , MAX2221X_SNSF_INVALID }
```

相关声明：[max2221x_snsf](#ga5992183c2872bcf60726fb32784099c8)、[MAX2221X_SNSF_FULL_SCALE](#gga5992183c2872bcf60726fb32784099c8a4028f111fbb042857cda1c38c07ea773)、[MAX2221X_SNSF_2_3](#gga5992183c2872bcf60726fb32784099c8a0cc4a45f17522eb715f9a515af2edd76)、[MAX2221X_SNSF_1_3](#gga5992183c2872bcf60726fb32784099c8aeabf1fd560e09cd18cd3279248dd81ee)、[MAX2221X_SNSF_INVALID](#gga5992183c2872bcf60726fb32784099c8a4c9960e70786dd5945ffb1f4d7b18b44)。

检测滤波器选项（Sense Filter Options）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga5794ef47813b578767bf8d22c817bfc5"></a>

```c
int max2221x_set_master_chop_freq (const struct device *dev, enum max2221x_master_chop_freq freq)
```

相关声明：[max2221x_set_master_chop_freq](#ga5794ef47813b578767bf8d22c817bfc5)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_master_chop_freq](#ga8f702fe056959c707d495a5b49ec7647)。

设置 MAX2221X 设备的主斩波频率（Master Chopping Frequency）。

<a id="r_gad283a38e9b32e9e721163feb2a7dc036"></a>

```c
int max2221x_get_master_chop_freq (const struct device *dev)
```

相关声明：[max2221x_get_master_chop_freq](#gad283a38e9b32e9e721163feb2a7dc036)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAX2221X 设备的主斩波频率（Master Chop Frequency）。

<a id="r_ga901b52fb1532c16cec31dc057085fb36"></a>

```c
int max2221x_get_channel_freq (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_channel_freq](#ga901b52fb1532c16cec31dc057085fb36)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备的通道频率（Channel Frequency）。

<a id="r_ga7eb45420e87a9dcb9642687208255d76"></a>

```c
int max2221x_set_part_state (const struct device *dev, bool enable)
```

相关声明：[max2221x_set_part_state](#ga7eb45420e87a9dcb9642687208255d76)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 MAX2221X 设备的器件状态（Part State），即启用或禁用。

<a id="r_ga50da67dab16f368b83125cb6ffcdf173"></a>

```c
int max2221x_set_channel_state (const struct device *dev, uint8_t channel, bool enable)
```

相关声明：[max2221x_set_channel_state](#ga50da67dab16f368b83125cb6ffcdf173)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 MAX2221X 设备某个通道的通道状态（Channel State），即启用或禁用。

<a id="r_gaa1ed035adbbe144a7637a86011d9e88c"></a>

```c
int max2221x_mask_fault_pin (const struct device *dev, enum max2221x_fault_pin_masks mask)
```

相关声明：[max2221x_mask_fault_pin](#gaa1ed035adbbe144a7637a86011d9e88c)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_fault_pin_masks](#ga399738e28a4b7c309137d674e433ccb6)。

屏蔽 MAX2221X 设备对某种故障条件（Fault Condition）的检测。

<a id="r_ga44a628faff5a7bdd9117a272db2bf76b"></a>

```c
int max2221x_unmask_fault_pin (const struct device *dev, enum max2221x_fault_pin_masks mask)
```

相关声明：[max2221x_unmask_fault_pin](#ga44a628faff5a7bdd9117a272db2bf76b)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_fault_pin_masks](#ga399738e28a4b7c309137d674e433ccb6)。

取消屏蔽 MAX2221X 设备对某种故障条件（Fault Condition）的检测。

<a id="r_ga0de71917ab9598525fce343c2b451edf"></a>

```c
int max2221x_set_vdr_mode (const struct device *dev, enum max2221x_vdr_mode mode)
```

相关声明：[max2221x_set_vdr_mode](#ga0de71917ab9598525fce343c2b451edf)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_vdr_mode](#gafced3b909c7963f0711bb23eecb4b538)。

设置 MAX2221X 设备的 VDR 模式（VDR Mode）。

<a id="r_ga53d4b2faaee0b83b08729619dd42187d"></a>

```c
int max2221x_get_vdr_mode (const struct device *dev)
```

相关声明：[max2221x_get_vdr_mode](#ga53d4b2faaee0b83b08729619dd42187d)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAX2221X 设备的 VDR 模式（VDR Mode）。

<a id="r_ga239238ccddb28147365069850333701e"></a>

```c
int max2221x_read_status (const struct device *dev, uint16_t *status)
```

相关声明：[max2221x_read_status](#ga239238ccddb28147365069850333701e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 MAX2221X 设备的状态（Status）。

<a id="r_ga0bd0b33a3020ccf22e726c38cf41dfd2"></a>

```c
int max2221x_read_vm_monitor (const struct device *dev, uint16_t *vm_monitor)
```

相关声明：[max2221x_read_vm_monitor](#ga0bd0b33a3020ccf22e726c38cf41dfd2)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 MAX2221X 设备的电压监测器（Voltage Monitor）。

<a id="r_ga420b8f7c31431a9f44655301e348993e"></a>

```c
int max2221x_set_dc_h2l (const struct device *dev, uint16_t dc_hdl)
```

相关声明：[max2221x_set_dc_h2l](#ga420b8f7c31431a9f44655301e348993e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 MAX2221X 设备的退磁电压（Demagnetization Voltage）。

<a id="r_gab7183c6bfa2c4ebf738f78d7a241d51e"></a>

```c
int max2221x_get_dc_h2l (const struct device *dev, uint16_t *dc_hdl)
```

相关声明：[max2221x_get_dc_h2l](#gab7183c6bfa2c4ebf738f78d7a241d51e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 MAX2221X 设备的退磁电压（Demagnetization Voltage）。

<a id="r_ga739a217f8e2e3518ca7223a05ea27f71"></a>

```c
int max2221x_set_vm_upper_threshold (const struct device *dev, enum max2221x_vm_threshold threshold)
```

相关声明：[max2221x_set_vm_upper_threshold](#ga739a217f8e2e3518ca7223a05ea27f71)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_vm_threshold](#ga37baf31388784ee8bcd4204a9520b60c)。

设置 MAX2221X 设备供电电压监测器的上阈值（Supply Voltage Monitor Upper Threshold）。

<a id="r_gac4d790ac301b3d2f0f17973ee631ce9a"></a>

```c
int max2221x_get_vm_upper_threshold (const struct device *dev)
```

相关声明：[max2221x_get_vm_upper_threshold](#gac4d790ac301b3d2f0f17973ee631ce9a)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAX2221X 设备供电电压监测器的上阈值（Supply Voltage Monitor Upper Threshold）。

<a id="r_ga8d417bccd2b1f015c8b985d0f8e64a41"></a>

```c
int max2221x_set_vm_lower_threshold (const struct device *dev, enum max2221x_vm_threshold threshold)
```

相关声明：[max2221x_set_vm_lower_threshold](#ga8d417bccd2b1f015c8b985d0f8e64a41)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_vm_threshold](#ga37baf31388784ee8bcd4204a9520b60c)。

设置 MAX2221X 设备供电电压监测器的下阈值（Supply Voltage Monitor Lower Threshold）。

<a id="r_gad3b27b5c1c43b05c4a80f1e3e9f9e4d3"></a>

```c
int max2221x_get_vm_lower_threshold (const struct device *dev)
```

相关声明：[max2221x_get_vm_lower_threshold](#gad3b27b5c1c43b05c4a80f1e3e9f9e4d3)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAX2221X 设备供电电压监测器的下阈值（Supply Voltage Monitor Lower Threshold）。

<a id="r_ga2d7680a00b951abb41cdf675c7d8346f"></a>

```c
int max2221x_read_dc_l2h (const struct device *dev, uint16_t *dc_l2h, uint8_t channel)
```

相关声明：[max2221x_read_dc_l2h](#ga2d7680a00b951abb41cdf675c7d8346f)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 MAX2221X 设备某个通道的 `DC_L2H` 值。

<a id="r_ga8075ed8e12d52083db84ba6f8756adb9"></a>

```c
int max2221x_write_dc_l2h (const struct device *dev, uint16_t dc_l2h, uint8_t channel)
```

相关声明：[max2221x_write_dc_l2h](#ga8075ed8e12d52083db84ba6f8756adb9)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 MAX2221X 设备某个通道的 `DC_L2H` 值。

<a id="r_gabf7cff9f7007a8a68d4b325beb4aa91a"></a>

```c
int max2221x_read_dc_h (const struct device *dev, uint16_t *dc_h, uint8_t channel)
```

相关声明：[max2221x_read_dc_h](#gabf7cff9f7007a8a68d4b325beb4aa91a)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 MAX2221X 设备某个通道的 `DC_H` 值。

<a id="r_gaf60031b728ef83a515b6636c309b22d4"></a>

```c
int max2221x_write_dc_h (const struct device *dev, uint16_t dc_h, uint8_t channel)
```

相关声明：[max2221x_write_dc_h](#gaf60031b728ef83a515b6636c309b22d4)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 MAX2221X 设备某个通道的 `DC_H` 值。

<a id="r_ga59f7c6e2f29293dc0c7583b0375bab6f"></a>

```c
int max2221x_read_dc_l (const struct device *dev, uint16_t *dc_l, uint8_t channel)
```

相关声明：[max2221x_read_dc_l](#ga59f7c6e2f29293dc0c7583b0375bab6f)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 MAX2221X 设备某个通道的 `DC_L` 值。

<a id="r_ga529818caa433e8b089f8d7948684ea93"></a>

```c
int max2221x_write_dc_l (const struct device *dev, uint16_t dc_l, uint8_t channel)
```

相关声明：[max2221x_write_dc_l](#ga529818caa433e8b089f8d7948684ea93)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 MAX2221X 设备某个通道的 `DC_L` 值。

<a id="r_ga65acdb4bb13a934ed399c353e9c3501b"></a>

```c
int max2221x_read_time_l2h (const struct device *dev, uint16_t *time_l2h, uint8_t channel)
```

相关声明：[max2221x_read_time_l2h](#ga65acdb4bb13a934ed399c353e9c3501b)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 MAX2221X 设备某个通道的 L2H 时间值（Time L2H）。

<a id="r_ga5583299893b1e824ebac01447a6edb8d"></a>

```c
int max2221x_write_time_l2h (const struct device *dev, uint16_t time_l2h, uint8_t channel)
```

相关声明：[max2221x_write_time_l2h](#ga5583299893b1e824ebac01447a6edb8d)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 MAX2221X 设备某个通道的 L2H 时间值（Time L2H）。

<a id="r_ga5a68165e4f5fbb0e6934572cd881889a"></a>

```c
int max2221x_set_ctrl_mode (const struct device *dev, enum max2221x_ctrl_mode mode, uint8_t channel)
```

相关声明：[max2221x_set_ctrl_mode](#ga5a68165e4f5fbb0e6934572cd881889a)、[device](../device_reference/P002_设备对象结构.md)、[max2221x_ctrl_mode](#gaef62d32791c1393a527bb26f7a42173f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 MAX2221X 设备某个通道的控制模式（Control Mode）。

<a id="r_ga5ad18cc556e62e132e878455c4cf5a4c"></a>

```c
int max2221x_get_ctrl_mode (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_ctrl_mode](#ga5ad18cc556e62e132e878455c4cf5a4c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的控制模式（Control Mode）。

<a id="r_ga0cc46ca9e0437199b9a6685220c71ac1"></a>

```c
int max2221x_set_ramps (const struct device *dev, uint8_t channel, uint8_t ramp_mask, bool enable)
```

相关声明：[max2221x_set_ramps](#ga0cc46ca9e0437199b9a6685220c71ac1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 MAX2221X 设备某个通道的斜坡（Ramps）。

<a id="r_ga9594a02a5cbf929acd982b7b93a5d4f8"></a>

```c
int max2221x_set_ramp_slew_rate (const struct device *dev, uint8_t channel, uint8_t ramp_slew_rate)
```

相关声明：[max2221x_set_ramp_slew_rate](#ga9594a02a5cbf929acd982b7b93a5d4f8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 MAX2221X 设备某个通道的斜坡变化速率（Ramp Slew Rate）。

<a id="r_ga460a8a4be932da15268029c4785a022d"></a>

```c
int max2221x_get_ramp_slew_rate (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_ramp_slew_rate](#ga460a8a4be932da15268029c4785a022d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的斜坡变化速率（Ramp Slew Rate）。

<a id="r_gaf3669424679108bafd9cf6ec9fdff1d1"></a>

```c
int max2221x_set_channel_chop_freq_div (const struct device *dev, uint8_t channel, enum max2221x_ch_freq_div freq_div)
```

相关声明：[max2221x_set_channel_chop_freq_div](#gaf3669424679108bafd9cf6ec9fdff1d1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max2221x_ch_freq_div](#ga2e92402dac3bd8036d0f1eff3e546c62)。

设置 MAX2221X 设备某个通道的斩波频率分频系数（Chopping Frequency Divider）。

<a id="r_gac1cd8396c8b72a60083727cc8ce6c79f"></a>

```c
int max2221x_get_channel_chop_freq_div (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_channel_chop_freq_div](#gac1cd8396c8b72a60083727cc8ce6c79f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的斩波频率分频系数（Chopping Frequency Divider）。

<a id="r_gab671df1d71393c7a83772aa90d525c38"></a>

```c
int max2221x_set_slew_rate (const struct device *dev, uint8_t channel, enum max2221x_slew_rate slew_rate)
```

相关声明：[max2221x_set_slew_rate](#gab671df1d71393c7a83772aa90d525c38)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max2221x_slew_rate](#gac3d8284e33a2cbc88e6e08396f6a2a66)。

设置 MAX2221X 设备某个通道的压摆率（Slew Rate）。

<a id="r_ga573d3cfca5ba3267a36c5817996d4f46"></a>

```c
int max2221x_get_slew_rate (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_slew_rate](#ga573d3cfca5ba3267a36c5817996d4f46)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的压摆率（Slew Rate）。

<a id="r_ga2a553f33ccbea8780cd5aa6e8259b14d"></a>

```c
int max2221x_set_gain (const struct device *dev, uint8_t channel, enum max2221x_gain gain)
```

相关声明：[max2221x_set_gain](#ga2a553f33ccbea8780cd5aa6e8259b14d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max2221x_gain](#ga064959a318df5a214758a95bc11ae8ed)。

设置 MAX2221X 设备某个通道 CDR 的数字增益（Digital Gain）。

<a id="r_gaa76a1ff0edc8b403850d687b67006529"></a>

```c
int max2221x_get_gain (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_gain](#gaa76a1ff0edc8b403850d687b67006529)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道 CDR 的数字增益（Digital Gain）。

<a id="r_ga4c7ad2ac6af19be09ac4efef35fc9c60"></a>

```c
int max2221x_set_snsf (const struct device *dev, uint8_t channel, enum max2221x_snsf snsf)
```

相关声明：[max2221x_set_snsf](#ga4c7ad2ac6af19be09ac4efef35fc9c60)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max2221x_snsf](#ga5992183c2872bcf60726fb32784099c8)。

设置 MAX2221X 设备某个通道的检测缩放系数（Sense Scaling Factor）。

<a id="r_ga441315200d66d8a798e76c59541573e9"></a>

```c
int max2221x_get_snsf (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_snsf](#ga441315200d66d8a798e76c59541573e9)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的检测缩放系数（Sense Scaling Factor）。

<a id="r_ga6a3c9546787e80fb421ff57c1aafd24a"></a>

```c
int max2221x_read_pwm_dutycycle (const struct device *dev, uint8_t channel, uint16_t *duty_cycle)
```

相关声明：[max2221x_read_pwm_dutycycle](#ga6a3c9546787e80fb421ff57c1aafd24a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 MAX2221X 设备某个通道的 PWM 占空比（Duty Cycle）。

<a id="r_ga5cc590f6f648ba1ff8cb96b369c1ea08"></a>

```c
int max2221x_read_fault0 (const struct device *dev)
```

相关声明：[max2221x_read_fault0](#ga5cc590f6f648ba1ff8cb96b369c1ea08)、[device](../device_reference/P002_设备对象结构.md)。

从 MAX2221X 设备的 `FAULT0` 寄存器读取故障状态（Fault Status）。

<a id="r_ga10fd9d6523ae83bb469076763f106fc1"></a>

```c
int max2221x_read_fault1 (const struct device *dev)
```

相关声明：[max2221x_read_fault1](#ga10fd9d6523ae83bb469076763f106fc1)、[device](../device_reference/P002_设备对象结构.md)。

从 MAX2221X 设备的 `FAULT1` 寄存器读取故障状态（Fault Status）。

<a id="r_ga6255d9e0310281eccfacad971987a327"></a>

```c
int max2221x_set_on_time (const struct device *dev, uint8_t channel, uint16_t on_time_us)
```

相关声明：[max2221x_set_on_time](#ga6255d9e0310281eccfacad971987a327)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 MAX2221X 设备某个通道的导通时间（On Time）。

<a id="r_ga685d70f78696d370acf9b0793121b24f"></a>

```c
int max2221x_get_on_time (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_on_time](#ga685d70f78696d370acf9b0793121b24f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的导通时间（On Time）。

<a id="r_ga8e767d8da3317ca745c956a3758e4f1b"></a>

```c
int max2221x_set_off_time (const struct device *dev, uint8_t channel, uint16_t off_time_us)
```

相关声明：[max2221x_set_off_time](#ga8e767d8da3317ca745c956a3758e4f1b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 MAX2221X 设备某个通道的关断时间（Off Time）。

<a id="r_ga7c78fbdcb856d34abbf061d292b4bebb"></a>

```c
int max2221x_get_off_time (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_off_time](#ga7c78fbdcb856d34abbf061d292b4bebb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的关断时间（Off Time）。

<a id="r_gaaed34f21363e832ff1db043a990c4c31"></a>

```c
int max2221x_set_stop_state (const struct device *dev, uint8_t channel, bool stop_state)
```

相关声明：[max2221x_set_stop_state](#gaaed34f21363e832ff1db043a990c4c31)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 MAX2221X 设备某个通道的停止状态（Stop State）。

<a id="r_gaafbc14d8bbdb5764e42b6e6ed5594122"></a>

```c
int max2221x_get_stop_state (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_stop_state](#gaafbc14d8bbdb5764e42b6e6ed5594122)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的停止状态（Stop State）。

<a id="r_gae0c2320ed0790377ad1b3390a060db49"></a>

```c
int max2221x_set_repetitions (const struct device *dev, uint8_t channel, uint16_t repetitions)
```

相关声明：[max2221x_set_repetitions](#gae0c2320ed0790377ad1b3390a060db49)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 MAX2221X 设备某个通道的重复次数（Repetitions）。

<a id="r_ga94eb711a8039d9eacfc254bf26ddcf39"></a>

```c
int max2221x_get_repetitions (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_get_repetitions](#ga94eb711a8039d9eacfc254bf26ddcf39)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 MAX2221X 设备某个通道的重复次数（Repetitions）。

<a id="r_gaa8a88aebc1d8c5d8290514b540574c28"></a>

```c
int max2221x_start_rapid_fire (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_start_rapid_fire](#gaa8a88aebc1d8c5d8290514b540574c28)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启动 MAX2221X 设备某个通道的快速连续触发模式（Rapid Fire Mode）。

<a id="r_ga6dc255318516cff52662d7c5533a0f74"></a>

```c
int max2221x_stop_rapid_fire (const struct device *dev, uint8_t channel)
```

相关声明：[max2221x_stop_rapid_fire](#ga6dc255318516cff52662d7c5533a0f74)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

停止 MAX2221X 设备某个通道的快速连续触发模式（Rapid Fire Mode）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 4.4\_MAX2221X 斜坡使能／禁用掩码（MAX2221X Ramp Enable/Disable Masks）

<a id="r_gae933f32f8cf7328dca2afb7f344dcb29"></a>

```c
#define MAX2221X_RAMP_DOWN_MASK BIT(2)
```

相关声明：[MAX2221X_RAMP_DOWN_MASK](#gae933f32f8cf7328dca2afb7f344dcb29)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

下降斜坡使能掩码（Ramp-down Enable Mask）。

<a id="r_gacb47da8940b93285c56693dee2aca071"></a>

```c
#define MAX2221X_RAMP_MID_MASK BIT(1)
```

相关声明：[MAX2221X_RAMP_MID_MASK](#gacb47da8940b93285c56693dee2aca071)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

中间斜坡使能掩码（Ramp-middle Enable Mask）。

<a id="r_ga73042e2ff448d10d2b36135f1f2fd27e"></a>

```c
#define MAX2221X_RAMP_UP_MASK BIT(0)
```

相关声明：[MAX2221X_RAMP_UP_MASK](#ga73042e2ff448d10d2b36135f1f2fd27e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

上升斜坡使能掩码（Ramp-up Enable Mask）。

## 4.5\_详细说明（Detailed Documentation）

<a id="gae933f32f8cf7328dca2afb7f344dcb29"></a>

### `MAX2221X_RAMP_DOWN_MASK`

```c
#define MAX2221X_RAMP_DOWN_MASK BIT(2)
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

下降斜坡使能掩码（Ramp-down Enable Mask）。

<a id="gacb47da8940b93285c56693dee2aca071"></a>

### `MAX2221X_RAMP_MID_MASK`

```c
#define MAX2221X_RAMP_MID_MASK BIT(1)
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

中间斜坡使能掩码（Ramp-middle Enable Mask）。

<a id="ga73042e2ff448d10d2b36135f1f2fd27e"></a>

### `MAX2221X_RAMP_UP_MASK`

```c
#define MAX2221X_RAMP_UP_MASK BIT(0)
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

上升斜坡使能掩码（Ramp-up Enable Mask）。

<a id="ga2e92402dac3bd8036d0f1eff3e546c62"></a>

### `max2221x_ch_freq_div`

```c
enum max2221x_ch_freq_div
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

通道频率分频系数选项（Channel Frequency Divisor Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_CH_FREQ_DIV_1` | 不分频（No Frequency Division）。 |
| `MAX2221X_CH_FREQ_DIV_2` | 频率二分频（Divided by 2）。 |
| `MAX2221X_CH_FREQ_DIV_4` | 频率四分频（Divided by 4）。 |
| `MAX2221X_CH_FREQ_DIV_8` | 频率八分频（Divided by 8）。 |
| `MAX2221X_CH_FREQ_DIV_INVALID` | 无效分频系数哨兵值（Invalid Frequency Divisor Sentinel）。 |

<a id="gaef62d32791c1393a527bb26f7a42173f"></a>

### `max2221x_ctrl_mode`

```c
enum max2221x_ctrl_mode
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

控制模式选项（Control Mode Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_CTRL_MODE_VOLT` | 电压驱动模式（Voltage Drive Mode）。 |
| `MAX2221X_CTRL_MODE_CDR` | 电流驱动模式（Current Drive Mode）。 |
| `MAX2221X_CTRL_MODE_LIMITER_VOLT` | 带电流限制器的电压驱动模式（Voltage Drive with Current Limiter Mode）。 |
| `MAX2221X_CTRL_MODE_VOLT_CDR` | 电压与电流驱动模式（Voltage and Current Drive Mode）。 |
| `MAX2221X_CTRL_MODE_INVALID` | 无效控制模式哨兵值（Invalid Control Mode Sentinel）。 |

<a id="ga399738e28a4b7c309137d674e433ccb6"></a>

### `max2221x_fault_pin_masks`

```c
enum max2221x_fault_pin_masks
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

故障引脚掩码定义（Fault Pin Mask Definitions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_FAULT_PIN_UVM` | 欠压监测故障（Under Voltage Monitor Fault）。 |
| `MAX2221X_FAULT_PIN_COMF` | 通信错误故障（Communication Error Fault）。 |
| `MAX2221X_FAULT_PIN_DPM` | DPM 错误故障（DPM Error Fault）。 |
| `MAX2221X_FAULT_PIN_HHF` | 未达到吸合电流（Hit Current）的错误故障。 |
| `MAX2221X_FAULT_PIN_OLF` | 开路负载故障（Open-Load Fault）。 |
| `MAX2221X_FAULT_PIN_OCP` | 过流保护故障（Over-Current Protection Fault）。 |
| `MAX2221X_FAULT_PIN_OVT` | 过温保护故障（Over-Temperature Protection Fault）。 |
| `MAX2221X_FAULT_PIN_INVALID` | 无效故障引脚哨兵值（Invalid Fault Pin Sentinel）。 |

<a id="ga064959a318df5a214758a95bc11ae8ed"></a>

### `max2221x_gain`

```c
enum max2221x_gain
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

增益缩放选项（Gain Scale Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_SCALE_1` | 增益比例因子（Gain Scale Factor）为 1。 |
| `MAX2221X_SCALE_2` | 增益比例因子（Gain Scale Factor）为 2。 |
| `MAX2221X_SCALE_3` | 增益比例因子（Gain Scale Factor）为 3。 |
| `MAX2221X_SCALE_4` | 增益比例因子（Gain Scale Factor）为 4。 |
| `MAX2221X_GAIN_INVALID` | 无效增益哨兵值（Invalid Gain Sentinel）。 |

<a id="ga41010c75c9cb6ed23e06cfec0ebbe413"></a>

### `max2221x_individual_chop_freq`

```c
enum max2221x_individual_chop_freq
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

独立通道斩波频率分频系数（Chopping Frequency Divisor）选项。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_FREQ_M` | 主频率（Master Frequency），不分频。 |
| `MAX2221X_FREQ_M_2` | 主频率（Master Frequency）二分频。 |
| `MAX2221X_FREQ_M_4` | 主频率（Master Frequency）四分频。 |
| `MAX2221X_FREQ_M_8` | 主频率（Master Frequency）八分频。 |
| `MAX2221X_FREQ_M_INVALID` | 无效分频系数哨兵值（Invalid Frequency Divisor Sentinel）。 |

<a id="ga8f702fe056959c707d495a5b49ec7647"></a>

### `max2221x_master_chop_freq`

```c
enum max2221x_master_chop_freq
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

主斩波频率（Master Chopping Frequency）选项。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_FREQ_100KHZ` | 频率（Frequency）为 100 kHz。 |
| `MAX2221X_FREQ_80KHZ` | 频率（Frequency）为 80 kHz。 |
| `MAX2221X_FREQ_60KHZ` | 频率（Frequency）为 60 kHz。 |
| `MAX2221X_FREQ_50KHZ` | 频率（Frequency）为 50 kHz。 |
| `MAX2221X_FREQ_40KHZ` | 频率（Frequency）为 40 kHz。 |
| `MAX2221X_FREQ_30KHZ` | 频率（Frequency）为 30 kHz。 |
| `MAX2221X_FREQ_25KHZ` | 频率（Frequency）为 25 kHz。 |
| `MAX2221X_FREQ_20KHZ` | 频率（Frequency）为 20 kHz。 |
| `MAX2221X_FREQ_15KHZ` | 频率（Frequency）为 15 kHz。 |
| `MAX2221X_FREQ_10KHZ` | 10 千赫（kHz）。 |
| `MAX2221X_FREQ_7500HZ` | 频率（Frequency）为 7.5 kHz。 |
| `MAX2221X_FREQ_5000HZ` | 5 千赫（kHz）。 |
| `MAX2221X_FREQ_2500HZ` | 频率（Frequency）为 2.5 kHz。 |
| `MAX2221X_FREQ_INVALID` | 无效频率哨兵值（Invalid Frequency Sentinel）。 |

<a id="gac3d8284e33a2cbc88e6e08396f6a2a66"></a>

### `max2221x_slew_rate`

```c
enum max2221x_slew_rate
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

压摆率选项（Slew Rate Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_SLEW_RATE_FAST` | 快速转换速率（Fast Slew Rate）。 |
| `MAX2221X_SLEW_RATE_400V_PER_US` | 转换速率（Slew Rate）为 400 V/µs。 |
| `MAX2221X_SLEW_RATE_200V_PER_US` | 转换速率（Slew Rate）为 200 V/µs。 |
| `MAX2221X_SLEW_RATE_100V_PER_US` | 转换速率（Slew Rate）为 100 V/µs。 |
| `MAX2221X_SLEW_RATE_INVALID` | 无效转换速率哨兵值（Invalid Slew Rate Sentinel）。 |

<a id="ga5992183c2872bcf60726fb32784099c8"></a>

### `max2221x_snsf`

```c
enum max2221x_snsf
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

检测滤波器选项（Sense Filter Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_SNSF_FULL_SCALE` | 满量程检测滤波器（Full Scale Sense Filter）。 |
| `MAX2221X_SNSF_2_3` | 2/3 量程检测滤波器（Sense Filter）。 |
| `MAX2221X_SNSF_1_3` | 1/3 量程检测滤波器（Sense Filter）。 |
| `MAX2221X_SNSF_INVALID` | 无效检测滤波器哨兵值（Invalid Sense Filter Sentinel）。 |

<a id="gafced3b909c7963f0711bb23eecb4b538"></a>

### `max2221x_vdr_mode`

```c
enum max2221x_vdr_mode
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

VDR 模式选项（VDR Mode Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_VDR_MODE_NORMAL` | 正常电压模式（Normal Voltage Mode）。 |
| `MAX2221X_VDR_MODE_DUTY` | 占空比模式（Duty Cycle Mode）。 |
| `MAX2221X_VDR_MODE_INVALID` | 无效电压驱动（VDR）模式哨兵值。 |

<a id="ga37baf31388784ee8bcd4204a9520b60c"></a>

### `max2221x_vm_threshold`

```c
enum max2221x_vm_threshold
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

VM 阈值电压等级（VM Threshold Voltage Levels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MAX2221X_VM_THRESHOLD_DISABLED` | 阈值（Threshold）已禁用。 |
| `MAX2221X_VM_THRESHOLD_4500MV` | 阈值（Threshold）为 4500 mV。 |
| `MAX2221X_VM_THRESHOLD_6500MV` | 阈值（Threshold）为 6500 mV。 |
| `MAX2221X_VM_THRESHOLD_8500MV` | 阈值（Threshold）为 8500 mV。 |
| `MAX2221X_VM_THRESHOLD_10500MV` | 阈值（Threshold）为 10500 mV。 |
| `MAX2221X_VM_THRESHOLD_12500MV` | 阈值（Threshold）为 12500 mV。 |
| `MAX2221X_VM_THRESHOLD_14500MV` | 阈值（Threshold）为 14500 mV。 |
| `MAX2221X_VM_THRESHOLD_16500MV` | 阈值（Threshold）为 16500 mV。 |
| `MAX2221X_VM_THRESHOLD_18500MV` | 阈值（Threshold）为 18500 mV。 |
| `MAX2221X_VM_THRESHOLD_20500MV` | 阈值（Threshold）为 20500 mV。 |
| `MAX2221X_VM_THRESHOLD_22500MV` | 阈值（Threshold）为 22500 mV。 |
| `MAX2221X_VM_THRESHOLD_24500MV` | 阈值（Threshold）为 24500 mV。 |
| `MAX2221X_VM_THRESHOLD_26500MV` | 阈值（Threshold）为 26500 mV。 |
| `MAX2221X_VM_THRESHOLD_28500MV` | 阈值（Threshold）为 28500 mV。 |
| `MAX2221X_VM_THRESHOLD_30500MV` | 阈值（Threshold）为 30500 mV。 |
| `MAX2221X_VM_THRESHOLD_32500MV` | 阈值（Threshold）为 32500 mV。 |
| `MAX2221X_VM_THRESHOLD_INVALID` | 无效阈值哨兵值（Invalid Threshold Sentinel）。 |

<a id="gac1cd8396c8b72a60083727cc8ce6c79f"></a>

### `max2221x_get_channel_chop_freq_div()`

```c
int max2221x_get_channel_chop_freq_div ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道的斩波频率分频系数（Chopping Frequency Divider）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取斩波频率分频系数（Chopping Frequency Divider）的通道。 |

**返回（Returns）**：返回值：成功时为斩波频率分频系数（Chopping Frequency Divider），失败时为负错误码。

<a id="ga901b52fb1532c16cec31dc057085fb36"></a>

### `max2221x_get_channel_freq()`

```c
int max2221x_get_channel_freq ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备的通道频率（Channel Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要读取的通道（Channel）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga5ad18cc556e62e132e878455c4cf5a4c"></a>

### `max2221x_get_ctrl_mode()`

```c
int max2221x_get_ctrl_mode ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道的控制模式（Control Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取控制模式（Control Mode）的通道。 |

**返回（Returns）**：返回值：成功时为控制模式（Control Mode），失败时为负错误码。

<a id="gab7183c6bfa2c4ebf738f78d7a241d51e"></a>

### `max2221x_get_dc_h2l()`

```c
int max2221x_get_dc_h2l ( const struct device * dev, uint16_t * dc_hdl )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备的退磁电压（Demagnetization Voltage）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dc_hdl` | 指向用于存储退磁电压（Demagnetization Voltage）的变量的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gaa76a1ff0edc8b403850d687b67006529"></a>

### `max2221x_get_gain()`

```c
int max2221x_get_gain ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道 CDR 的数字增益（Digital Gain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取增益（Gain）的通道。 |

**返回（Returns）**：返回值：成功时为增益（Gain），失败时为负错误码。

<a id="gad283a38e9b32e9e721163feb2a7dc036"></a>

### `max2221x_get_master_chop_freq()`

```c
int max2221x_get_master_chop_freq ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备的主斩波频率（Master Chop Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：返回值：成功时为主斩波频率（Master Chop Frequency），单位为 Hz；失败时为负错误码。

<a id="ga7c78fbdcb856d34abbf061d292b4bebb"></a>

### `max2221x_get_off_time()`

```c
int max2221x_get_off_time ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道的关断时间（Off Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取关闭时间（Off Time）的通道。 |

**返回（Returns）**：返回值：成功时为关闭时间（Off Time），单位为微秒；失败时为负错误码。

<a id="ga685d70f78696d370acf9b0793121b24f"></a>

### `max2221x_get_on_time()`

```c
int max2221x_get_on_time ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道的导通时间（On Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取开启时间（On Time）的通道。 |

**返回（Returns）**：返回值：成功时为开启时间（On Time），单位为微秒；失败时为负错误码。

<a id="ga460a8a4be932da15268029c4785a022d"></a>

### `max2221x_get_ramp_slew_rate()`

```c
int max2221x_get_ramp_slew_rate ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道的斜坡变化速率（Ramp Slew Rate）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取斜坡转换速率（Ramp Slew Rate）的通道。 |

**返回（Returns）**：返回值：成功时为斜坡转换速率（Ramp Slew Rate），失败时为负错误码。

<a id="ga94eb711a8039d9eacfc254bf26ddcf39"></a>

### `max2221x_get_repetitions()`

```c
int max2221x_get_repetitions ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道的重复次数（Repetitions）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取重复次数（Repetitions）的通道。 |

**返回（Returns）**：返回值：成功时为重复次数（Repetitions），失败时为负错误码。

<a id="ga573d3cfca5ba3267a36c5817996d4f46"></a>

### `max2221x_get_slew_rate()`

```c
int max2221x_get_slew_rate ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道的压摆率（Slew Rate）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取转换速率（Slew Rate）的通道。 |

**返回（Returns）**：返回值：成功时为转换速率（Slew Rate），失败时为负错误码。

<a id="ga441315200d66d8a798e76c59541573e9"></a>

### `max2221x_get_snsf()`

```c
int max2221x_get_snsf ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道的检测缩放系数（Sense Scaling Factor）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取检测缩放因子（Sense Scaling Factor）的通道。 |

**返回（Returns）**：返回值：成功时为检测缩放因子（Sense Scaling Factor），失败时为负错误码。

<a id="gaafbc14d8bbdb5764e42b6e6ed5594122"></a>

### `max2221x_get_stop_state()`

```c
int max2221x_get_stop_state ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备某个通道的停止状态（Stop State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要获取停止状态（Stop State）的通道。 |

**返回（Returns）**：返回值：成功时为停止状态（Stop State），失败时为负错误码。

<a id="ga53d4b2faaee0b83b08729619dd42187d"></a>

### `max2221x_get_vdr_mode()`

```c
int max2221x_get_vdr_mode ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备的 VDR 模式（VDR Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：返回值：成功时为电压驱动（VDR）模式，失败时为负错误码。

<a id="gad3b27b5c1c43b05c4a80f1e3e9f9e4d3"></a>

### `max2221x_get_vm_lower_threshold()`

```c
int max2221x_get_vm_lower_threshold ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备供电电压监测器的下阈值（Supply Voltage Monitor Lower Threshold）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：返回值：成功时为下限阈值（Lower Threshold），单位为毫伏；失败时为负错误码。

<a id="gac4d790ac301b3d2f0f17973ee631ce9a"></a>

### `max2221x_get_vm_upper_threshold()`

```c
int max2221x_get_vm_upper_threshold ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

获取 MAX2221X 设备供电电压监测器的上阈值（Supply Voltage Monitor Upper Threshold）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：返回值：成功时为上限阈值（Upper Threshold），单位为毫伏；失败时为负错误码。

<a id="gaa1ed035adbbe144a7637a86011d9e88c"></a>

### `max2221x_mask_fault_pin()`

```c
int max2221x_mask_fault_pin ( const struct device * dev, enum max2221x_fault_pin_masks mask )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

屏蔽 MAX2221X 设备对某种故障条件（Fault Condition）的检测。

针对过流条件（Overcurrent Condition）屏蔽故障引脚（Fault Pin）。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_mask_fault_pin(dev, MAX2221X_FAULT_PIN_OCP);
if (ret)
    printk("Failed to mask fault pin: %d\n", ret);
else
    printk("Fault pin masked successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 要屏蔽的故障条件（Fault Condition）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gabf7cff9f7007a8a68d4b325beb4aa91a"></a>

### `max2221x_read_dc_h()`

```c
int max2221x_read_dc_h ( const struct device * dev, uint16_t * dc_h, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

读取 MAX2221X 设备某个通道的 `DC_H` 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dc_h` | 指向用于存储 `DC_H` 值的变量的指针。 |
| `channel` | 要从中读取 `DC_H` 值的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga59f7c6e2f29293dc0c7583b0375bab6f"></a>

### `max2221x_read_dc_l()`

```c
int max2221x_read_dc_l ( const struct device * dev, uint16_t * dc_l, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

读取 MAX2221X 设备某个通道的 `DC_L` 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dc_l` | 指向用于存储 `DC_L` 值的变量的指针。 |
| `channel` | 要从中读取 `DC_L` 值的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga2d7680a00b951abb41cdf675c7d8346f"></a>

### `max2221x_read_dc_l2h()`

```c
int max2221x_read_dc_l2h ( const struct device * dev, uint16_t * dc_l2h, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

读取 MAX2221X 设备某个通道的 `DC_L2H` 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dc_l2h` | 指向用于存储 `DC_L2H` 值的变量的指针。 |
| `channel` | 要从中读取 `DC_L2H` 值的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga5cc590f6f648ba1ff8cb96b369c1ea08"></a>

### `max2221x_read_fault0()`

```c
int max2221x_read_fault0 ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

从 MAX2221X 设备的 `FAULT0` 寄存器读取故障状态（Fault Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga10fd9d6523ae83bb469076763f106fc1"></a>

### `max2221x_read_fault1()`

```c
int max2221x_read_fault1 ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

从 MAX2221X 设备的 `FAULT1` 寄存器读取故障状态（Fault Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga6a3c9546787e80fb421ff57c1aafd24a"></a>

### `max2221x_read_pwm_dutycycle()`

```c
int max2221x_read_pwm_dutycycle ( const struct device * dev, uint8_t channel, uint16_t * duty_cycle )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

读取 MAX2221X 设备某个通道的 PWM 占空比（Duty Cycle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要从中读取脉宽调制占空比（PWM Duty Cycle）的通道。 |
| `duty_cycle` | 指向用于存储脉宽调制占空比（PWM Duty Cycle）的变量的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga239238ccddb28147365069850333701e"></a>

### `max2221x_read_status()`

```c
int max2221x_read_status ( const struct device * dev, uint16_t * status )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

读取 MAX2221X 设备的状态（Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `status` | 指向用于存储状态（Status）的变量的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga65acdb4bb13a934ed399c353e9c3501b"></a>

### `max2221x_read_time_l2h()`

```c
int max2221x_read_time_l2h ( const struct device * dev, uint16_t * time_l2h, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

读取 MAX2221X 设备某个通道的 L2H 时间值（Time L2H）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `time_l2h` | 指向用于存储低到高转换时间（Time L2H）值的变量的指针。 |
| `channel` | 要从中读取低到高转换时间（Time L2H）值的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga0bd0b33a3020ccf22e726c38cf41dfd2"></a>

### `max2221x_read_vm_monitor()`

```c
int max2221x_read_vm_monitor ( const struct device * dev, uint16_t * vm_monitor )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

读取 MAX2221X 设备的电压监测器（Voltage Monitor）。

VM 电压测量值（Measurement）按下式计算：

`VM = KVM x vm_monitor`，其中 `KVM = 9.73 mV`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `vm_monitor` | 指向用于存储电压监测值（Voltage Monitor）的变量的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gaf3669424679108bafd9cf6ec9fdff1d1"></a>

### `max2221x_set_channel_chop_freq_div()`

```c
int max2221x_set_channel_chop_freq_div ( const struct device * dev, uint8_t channel, enum max2221x_ch_freq_div freq_div )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的斩波频率分频系数（Chopping Frequency Divider）。

将通道的斩波频率分频系数（Chopping Frequency Divider）设为 1。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_set_channel_chop_freq_div(dev, channel, MAX2221X_CH_FREQ_DIV_1);
if (ret)
    printk("Failed to set channel chopping frequency divider: %d\n", ret);
else
    printk("Channel chopping frequency divider set successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置斩波频率分频系数（Chopping Frequency Divider）的通道。 |
| `freq_div` | 要设置的目标斩波频率分频系数（Chopping Frequency Divider）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga50da67dab16f368b83125cb6ffcdf173"></a>

### `max2221x_set_channel_state()`

```c
int max2221x_set_channel_state ( const struct device * dev, uint8_t channel, bool enable )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的通道状态（Channel State），即启用或禁用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置状态（State）的通道。 |
| `enable` | `true` 表示使能通道（Channel），`false` 表示禁用。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga5a68165e4f5fbb0e6934572cd881889a"></a>

### `max2221x_set_ctrl_mode()`

```c
int max2221x_set_ctrl_mode ( const struct device * dev, enum max2221x_ctrl_mode mode, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的控制模式（Control Mode）。

为通道 1 设置直流电机驱动（DC Motor Drive）的控制模式。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_set_ctrl_mode(dev, MAX2221X_CTRL_MODE_LIMITER_VOLT, 1);
if (ret)
    printk("Failed to set control mode: %d\n", ret);
else
    printk("Control mode set successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mode` | 要设置的目标控制模式（Control Mode）。 |
| `channel` | 要设置控制模式（Control Mode）的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga420b8f7c31431a9f44655301e348993e"></a>

### `max2221x_set_dc_h2l()`

```c
int max2221x_set_dc_h2l ( const struct device * dev, uint16_t dc_hdl )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备的退磁电压（Demagnetization Voltage）。

如果 `mode` 为 `MAX2221X_VDR_MODE_DUTY`，则 `dc_hdl` 表示电压，其值按 `VOUT (V) = KVDR x 36 x dc_hdl` 计算。如果 `mode` 为 `MAX2221X_VDR_MODE_NORMAL`，则 `dc_hdl` 表示占空比（Duty Cycle），电压按 `VOUT (V) = KVDR x VM x dc_hdl` 计算。其中 `KVDR = 30.518 uV`。译注：此处模式与公式的对应关系按官方本段原样保留；它与后续 DC_H／DC_L 说明中的 VDR、VDRDUTY 对应关系存在差异，使用时应核对驱动实现与器件定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dc_hdl` | 要设置的目标退磁电压（Demagnetization Voltage）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga2a553f33ccbea8780cd5aa6e8259b14d"></a>

### `max2221x_set_gain()`

```c
int max2221x_set_gain ( const struct device * dev, uint8_t channel, enum max2221x_gain gain )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道 CDR 的数字增益（Digital Gain）。

将通道 1 的增益（Gain）设为 1。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_set_gain(dev, 1, MAX2221X_SCALE_1);
if (ret)
    printk("Failed to set gain: %d\n", ret);
else
    printk("Gain set successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置增益（Gain）的通道。 |
| `gain` | 要设置的目标增益（Gain）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga5794ef47813b578767bf8d22c817bfc5"></a>

### `max2221x_set_master_chop_freq()`

```c
int max2221x_set_master_chop_freq ( const struct device * dev, enum max2221x_master_chop_freq freq )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备的主斩波频率（Master Chopping Frequency）。

将主斩波频率（Master Chop Frequency）设为 50 kHz。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_set_master_chop_freq(dev, MAX2221X_FREQ_50KHZ);
if (ret)
    printk("Failed to set master chop frequency: %d\n", ret);
else
    printk("Master chop frequency set successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `freq` | 要设置的目标主斩波频率（Master Chopping Frequency）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga8e767d8da3317ca745c956a3758e4f1b"></a>

### `max2221x_set_off_time()`

```c
int max2221x_set_off_time ( const struct device * dev, uint8_t channel, uint16_t off_time_us )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的关断时间（Off Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置关闭时间（Off Time）的通道。 |
| `off_time_us` | 要设置的目标关闭时间（Off Time），单位为微秒。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga6255d9e0310281eccfacad971987a327"></a>

### `max2221x_set_on_time()`

```c
int max2221x_set_on_time ( const struct device * dev, uint8_t channel, uint16_t on_time_us )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的导通时间（On Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置开启时间（On Time）的通道。 |
| `on_time_us` | 要设置的目标开启时间（On Time），单位为微秒。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga7eb45420e87a9dcb9642687208255d76"></a>

### `max2221x_set_part_state()`

```c
int max2221x_set_part_state ( const struct device * dev, bool enable )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备的器件状态（Part State），即启用或禁用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `enable` | `true` 表示使能器件（Part），`false` 表示禁用。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga9594a02a5cbf929acd982b7b93a5d4f8"></a>

### `max2221x_set_ramp_slew_rate()`

```c
int max2221x_set_ramp_slew_rate ( const struct device * dev, uint8_t channel, uint8_t ramp_slew_rate )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的斜坡变化速率（Ramp Slew Rate）。

设置斜坡转换速率（Ramp Slew Rate）。VDRDUTY 模式：`Ramp Slew Rate (V/ms) = KVDR x VM x (ramp_slew_rate + 1) x F_PWM (kHz)`；VDR 模式：`Ramp Slew Rate (V/ms) = KVDR x 36 x (ramp_slew_rate + 1) x F_PWM (kHz)`；CDR 模式：`Ramp Slew Rate (mA/ms) = KCDR x GAIN x SNSF x (ramp_slew_rate + 1) x F_PWM (kHz)`。

其中，`KVDR = 30.518 uV`；`KCDR` 对于 MAX22216 为 `1.017 mA`，对于 MAX22217 为 `0.339 mA`；`F_PWM` 为通道斩波频率（Channel Chopping Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置斜坡转换速率（Ramp Slew Rate）的通道。 |
| `ramp_slew_rate` | 要设置的目标斜坡转换速率（Ramp Slew Rate）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga0cc46ca9e0437199b9a6685220c71ac1"></a>

### `max2221x_set_ramps()`

```c
int max2221x_set_ramps ( const struct device * dev, uint8_t channel, uint8_t ramp_mask, bool enable )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的斜坡（Ramps）。

此基础函数根据 `enable` 参数使能或禁用斜坡（Ramps）。如需明确执行使能或禁用操作，请使用 `max2221x_enable_ramps()` 或 `max2221x_disable_ramps()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置斜坡（Ramps）的通道。 |
| `ramp_mask` | 指示要修改哪些斜坡的斜坡掩码（Ramp Mask）。 |
| `enable` | `true` 表示使能指定斜坡（Ramps），`false` 表示禁用。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gae0c2320ed0790377ad1b3390a060db49"></a>

### `max2221x_set_repetitions()`

```c
int max2221x_set_repetitions ( const struct device * dev, uint8_t channel, uint16_t repetitions )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的重复次数（Repetitions）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置重复次数（Repetitions）的通道。 |
| `repetitions` | 要设置的目标重复次数（Repetitions）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gab671df1d71393c7a83772aa90d525c38"></a>

### `max2221x_set_slew_rate()`

```c
int max2221x_set_slew_rate ( const struct device * dev, uint8_t channel, enum max2221x_slew_rate slew_rate )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的压摆率（Slew Rate）。

将通道 1 的转换速率（Slew Rate）设为 400 V/µs。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_set_slew_rate(dev, 1, MAX2221X_SLEW_RATE_400V_PER_US);
if (ret)
    printk("Failed to set slew rate: %d\n", ret);
else
    printk("Slew rate set successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置转换速率（Slew Rate）的通道。 |
| `slew_rate` | 要设置的目标转换速率（Slew Rate）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga4c7ad2ac6af19be09ac4efef35fc9c60"></a>

### `max2221x_set_snsf()`

```c
int max2221x_set_snsf ( const struct device * dev, uint8_t channel, enum max2221x_snsf snsf )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的检测缩放系数（Sense Scaling Factor）。

将通道 1 的检测缩放因子（Sense Scaling Factor）设为 2/3。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_set_snsf(dev, 1, MAX2221X_SNSF_2_3);
if (ret)
    printk("Failed to set sense scaling factor: %d\n", ret);
else
    printk("Sense scaling factor set successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置检测缩放因子（Sense Scaling Factor）的通道。 |
| `snsf` | 要设置的目标检测缩放因子（Sense Scaling Factor）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gaaed34f21363e832ff1db043a990c4c31"></a>

### `max2221x_set_stop_state()`

```c
int max2221x_set_stop_state ( const struct device * dev, uint8_t channel, bool stop_state )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备某个通道的停止状态（Stop State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要设置停止状态（Stop State）的通道。 |
| `stop_state` | 要设置的目标停止状态（Stop State）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga0de71917ab9598525fce343c2b451edf"></a>

### `max2221x_set_vdr_mode()`

```c
int max2221x_set_vdr_mode ( const struct device * dev, enum max2221x_vdr_mode mode )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备的 VDR 模式（VDR Mode）。

将电压驱动（VDR）模式设为 VDRDUTY。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_set_vdr_mode(dev, MAX2221X_VDR_MODE_DUTY);
if (ret)
    printk("Failed to set VDR mode: %d\n", ret);
else
    printk("VDR mode set successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mode` | 要设置的电压驱动（VDR）模式。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga8d417bccd2b1f015c8b985d0f8e64a41"></a>

### `max2221x_set_vm_lower_threshold()`

```c
int max2221x_set_vm_lower_threshold ( const struct device * dev, enum max2221x_vm_threshold threshold )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备供电电压监测器的下阈值（Supply Voltage Monitor Lower Threshold）。

将下限阈值（Lower Threshold）设为 4500 mV。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_set_vm_lower_threshold(dev, MAX2221X_VM_THRESHOLD_4500MV);
if (ret)
    printk("Failed to set lower threshold: %d\n", ret);
else
    printk("Lower threshold set successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `threshold` | 要设置的目标下限阈值（Lower Threshold）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga739a217f8e2e3518ca7223a05ea27f71"></a>

### `max2221x_set_vm_upper_threshold()`

```c
int max2221x_set_vm_upper_threshold ( const struct device * dev, enum max2221x_vm_threshold threshold )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

设置 MAX2221X 设备供电电压监测器的上阈值（Supply Voltage Monitor Upper Threshold）。

将上限阈值（Upper Threshold）设为 4500 mV。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_set_vm_upper_threshold(dev, MAX2221X_VM_THRESHOLD_4500MV);
if (ret)
    printk("Failed to set upper threshold: %d\n", ret);
else
    printk("Upper threshold set successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `threshold` | 要设置的目标上限阈值（Upper Threshold）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gaa8a88aebc1d8c5d8290514b540574c28"></a>

### `max2221x_start_rapid_fire()`

```c
int max2221x_start_rapid_fire ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

启动 MAX2221X 设备某个通道的快速连续触发模式（Rapid Fire Mode）。

设置快速重复驱动（Rapid Fire）参数并启动该模式。以下示例展示如何在启动前配置开启时间（On Time）1000 µs、关闭时间（Off Time）1000 µs、停止状态（Stop State）`true` 及重复次数（Repetitions）10。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret;
ret = max2221x_set_on_time(dev, channel, 1000);
if (ret) {
    printk("Failed to set on time: %d\n", ret);
    return ret;
}
ret = max2221x_set_off_time(dev, channel, 1000);
if (ret) {
    printk("Failed to set off time: %d\n", ret);
    return ret;
}
ret = max2221x_set_stop_state(dev, channel, true);
if (ret) {
    printk("Failed to set stop state: %d\n", ret);
    return ret;
}
ret = max2221x_set_repetitions(dev, channel, 10);
if (ret) {
    printk("Failed to set repetitions: %d\n", ret);
    return ret;
}
ret = max2221x_start_rapid_fire(dev, channel);
if (ret) {
    printk("Failed to start rapid fire mode: %d\n", ret);
} else {
    printk("Rapid fire mode started successfully\n");
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要启动快速重复驱动模式（Rapid Fire Mode）的通道。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时返回负错误码。 |

**说明（Note）**：注意：通常应先设置开启时间（On Time）、关闭时间（Off Time）、重复次数（Repetitions）和停止状态（Stop State），再启动快速重复驱动模式（Rapid Fire Mode）。

<a id="ga6dc255318516cff52662d7c5533a0f74"></a>

### `max2221x_stop_rapid_fire()`

```c
int max2221x_stop_rapid_fire ( const struct device * dev, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

停止 MAX2221X 设备某个通道的快速连续触发模式（Rapid Fire Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 要停止快速重复驱动模式（Rapid Fire Mode）的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga44a628faff5a7bdd9117a272db2bf76b"></a>

### `max2221x_unmask_fault_pin()`

```c
int max2221x_unmask_fault_pin ( const struct device * dev, enum max2221x_fault_pin_masks mask )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

取消屏蔽 MAX2221X 设备对某种故障条件（Fault Condition）的检测。

针对过流条件（Overcurrent Condition）解除故障引脚（Fault Pin）的屏蔽。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>

int ret = max2221x_unmask_fault_pin(dev, MAX2221X_FAULT_PIN_OCP);
if (ret)
    printk("Failed to unmask fault pin: %d\n", ret);
else
    printk("Fault pin unmasked successfully\n");
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 要解除屏蔽的故障条件（Fault Condition）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="gaf60031b728ef83a515b6636c309b22d4"></a>

### `max2221x_write_dc_h()`

```c
int max2221x_write_dc_h ( const struct device * dev, uint16_t dc_h, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

写入 MAX2221X 设备某个通道的 `DC_H` 值。

设置 `DC_H` 电平（Level）：VDR 模式下 `VOUT (V) = KVDR x 36 x dc_h`；VDRDUTY 模式下 `VOUT (V) = KVDR x VM x dc_h`；CDR 模式下 `IOUT (mA) = KCDR x GAIN x SNSF x dc_h`。其中 `KVDR = 30.518 uV`；`KCDR` 对于 MAX22216 为 `1.017 mA`，对于 MAX22217 为 `0.339 mA`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dc_h` | 要写入的目标 `DC_H` 值。 |
| `channel` | 要写入 `DC_H` 值的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga529818caa433e8b089f8d7948684ea93"></a>

### `max2221x_write_dc_l()`

```c
int max2221x_write_dc_l ( const struct device * dev, uint16_t dc_l, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

写入 MAX2221X 设备某个通道的 `DC_L` 值。

设置 `DC_L` 电平（Level）：VDR 模式下 `VOUT (V) = KVDR x 36 x dc_l`；VDRDUTY 模式下 `VOUT (V) = KVDR x VM x dc_l`；CDR 模式下 `IOUT (mA) = KCDR x GAIN x SNSF x dc_l`。其中 `KVDR = 30.518 uV`；`KCDR` 对于 MAX22216 为 `1.017 mA`，对于 MAX22217 为 `0.339 mA`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dc_l` | 要写入的目标 `DC_L` 值。 |
| `channel` | 要写入 `DC_L` 值的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga8075ed8e12d52083db84ba6f8756adb9"></a>

### `max2221x_write_dc_l2h()`

```c
int max2221x_write_dc_l2h ( const struct device * dev, uint16_t dc_l2h, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

写入 MAX2221X 设备某个通道的 `DC_L2H` 值。

设置 `DC_L2H` 电平（Level）：VDR 模式下 `VOUT (V) = KVDR x 36 x dc_l2h`；VDRDUTY 模式下 `VOUT (V) = KVDR x VM x dc_l2h`；CDR 模式下 `IOUT (mA) = KCDR x GAIN x SNSF x dc_l2h`。其中 `KVDR = 30.518 uV`；`KCDR` 对于 MAX22216 为 `1.017 mA`，对于 MAX22217 为 `0.339 mA`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `dc_l2h` | 要写入的目标 `DC_L2H` 值。 |
| `channel` | 要写入 `DC_L2H` 值的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。

<a id="ga5583299893b1e824ebac01447a6edb8d"></a>

### `max2221x_write_time_l2h()`

```c
int max2221x_write_time_l2h ( const struct device * dev, uint16_t time_l2h, uint8_t channel )
```

```c
#include <zephyr/drivers/misc/max2221x/max2221x.h>
```

写入 MAX2221X 设备某个通道的 L2H 时间值（Time L2H）。

设置低到高转换时间（Time L2H）：`TIME_L2H (s) = time_l2h / channel chopping frequency`，即 `time_l2h` 除以通道斩波频率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `time_l2h` | 要写入的目标低到高转换时间（Time L2H）值。 |
| `channel` | 要写入低到高转换时间（Time L2H）值的通道。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误码（Negative Error Code）。


## 4.6\_原页交叉引用（Cross References）

- [max2221x.h](../api_file_network_pcie_reference/P007_zephyr__drivers__misc__max2221x__max2221x.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [printk](../api_file_clock_network_reference/P019_zephyr__sys__printk.h_文件参考.md#a1bce54a738ce2d9dd6d95ee842ec237c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga2e92402dac3bd8036d0f1eff3e546c62ac69bf198154fd6084bdc981e1337b063"></a>
<a id="gga2e92402dac3bd8036d0f1eff3e546c62ae8d46ab082eaf0ffea37eba0af34644e"></a>
<a id="gga2e92402dac3bd8036d0f1eff3e546c62aed3e437b171469464e72ff0b3b28b7a9"></a>
<a id="gga2e92402dac3bd8036d0f1eff3e546c62a85d1c13f410bc24356f8e93bd31c7f5e"></a>
<a id="gga2e92402dac3bd8036d0f1eff3e546c62af01c9a7f7826740ebc76db2d091c476f"></a>
<a id="ggaef62d32791c1393a527bb26f7a42173fa372f7920212b45635bb3ab73e524d3b6"></a>
<a id="ggaef62d32791c1393a527bb26f7a42173faf006eb6ec53799777f20141e4b18ae65"></a>
<a id="ggaef62d32791c1393a527bb26f7a42173fa3df216e71e2e032db275a892de63de7c"></a>
<a id="ggaef62d32791c1393a527bb26f7a42173fa7ff1ba3a5cb0eba7d36cf3aacd1f3f36"></a>
<a id="ggaef62d32791c1393a527bb26f7a42173fa58053f83bdfef9587b04e9f122b28e76"></a>
<a id="gga399738e28a4b7c309137d674e433ccb6a9cf6ad6bb71092f7e28eb7de91e92a51"></a>
<a id="gga399738e28a4b7c309137d674e433ccb6a9492bcaf6e4e5e41bca5d156b7cbde92"></a>
<a id="gga399738e28a4b7c309137d674e433ccb6a12806ad411905619c15ed7cc603cdb36"></a>
<a id="gga399738e28a4b7c309137d674e433ccb6a28bb4d3f65348762116f5a14b6a4614f"></a>
<a id="gga399738e28a4b7c309137d674e433ccb6a5dcb7a29041c5ec4b399795cf59db322"></a>
<a id="gga399738e28a4b7c309137d674e433ccb6aae654309f343b46f117327afe025c789"></a>
<a id="gga399738e28a4b7c309137d674e433ccb6a1f2abcecc1b2ad5092322034797fa391"></a>
<a id="gga399738e28a4b7c309137d674e433ccb6a41a39797fc9dfc70c31f7fa08d083354"></a>
<a id="gga064959a318df5a214758a95bc11ae8eda5727a7f4e76cb429be734014a48790c8"></a>
<a id="gga064959a318df5a214758a95bc11ae8eda90b7f2ecaf5c15746dea522d68da29c5"></a>
<a id="gga064959a318df5a214758a95bc11ae8eda8d370b6484c4e6ed5ff0533175fa0db1"></a>
<a id="gga064959a318df5a214758a95bc11ae8eda3e5bf24a80ff6901a1de5946c79eb169"></a>
<a id="gga064959a318df5a214758a95bc11ae8edacadcdeeb9fccb6e7ad947824cb68fe91"></a>
<a id="gga41010c75c9cb6ed23e06cfec0ebbe413a4cee57aef5be5d79919513fea3891490"></a>
<a id="gga41010c75c9cb6ed23e06cfec0ebbe413a120c21fdf16a48795233bae403a0c3f1"></a>
<a id="gga41010c75c9cb6ed23e06cfec0ebbe413a84119a5bb314c03760637ebb05a7f16a"></a>
<a id="gga41010c75c9cb6ed23e06cfec0ebbe413ac0955ebf50e1c3d7a51e6aa42e008cfd"></a>
<a id="gga41010c75c9cb6ed23e06cfec0ebbe413af6f9cae164f70b5fc9a7003e526d15b2"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647ab689b993d9fa98c5bf140162723d2feb"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a1a478348731bd456313912f6b4a59f1f"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a93bf099ae22e26de9885c76bc8428eb8"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a1710af28d11faf44c423f2f771f02980"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a34a90a18c91e8e6f547c0788d4061612"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647ab4e2229b6516ea4f7278fa2931f262ed"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a8a11aacff6d925230f8719508b432cef"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a5cdbdb4c266cca9ae859f20dc0187a15"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647aa39e41621ac0f7f7073d95cfa18c99a4"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647abcaa72d42d74f8054480c73bf3fa61f5"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a208bff3bc2c214ea84404ba49c1037cb"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a0e56c34ed02843a63bbcfe0d219b2dbc"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a30dbf5e8aa5f7aa61cff6cf7391e39c9"></a>
<a id="gga8f702fe056959c707d495a5b49ec7647a2bfeae761213ed84221a6bda013599aa"></a>
<a id="ggac3d8284e33a2cbc88e6e08396f6a2a66a18b08f934c4c9923addad9e55ab9be5d"></a>
<a id="ggac3d8284e33a2cbc88e6e08396f6a2a66a6daf654eb4baaa6a59215fef63913a29"></a>
<a id="ggac3d8284e33a2cbc88e6e08396f6a2a66ad5a2520754e00735b2985c7627075e55"></a>
<a id="ggac3d8284e33a2cbc88e6e08396f6a2a66aa488670f38c32f36f37faf5421ab475b"></a>
<a id="ggac3d8284e33a2cbc88e6e08396f6a2a66afe236cb49bf00f23d386d36f0c8ea600"></a>
<a id="gga5992183c2872bcf60726fb32784099c8a4028f111fbb042857cda1c38c07ea773"></a>
<a id="gga5992183c2872bcf60726fb32784099c8a0cc4a45f17522eb715f9a515af2edd76"></a>
<a id="gga5992183c2872bcf60726fb32784099c8aeabf1fd560e09cd18cd3279248dd81ee"></a>
<a id="gga5992183c2872bcf60726fb32784099c8a4c9960e70786dd5945ffb1f4d7b18b44"></a>
<a id="ggafced3b909c7963f0711bb23eecb4b538afe372c1bf8c9c3393600ffe8edaaf103"></a>
<a id="ggafced3b909c7963f0711bb23eecb4b538a0eb8adae84e34d4bec22326d14ecfabc"></a>
<a id="ggafced3b909c7963f0711bb23eecb4b538a4d90473664901f26df9f23dea49ddc81"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60cab2f1292ea8d5a4f57c7a267b7a5996b2"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60cae739f6bd1a1d4278a307ea35a0403f89"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60caa46a4fc4d6a929fbd18010a0720f3e34"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60ca3b338a5c0c21c80dddbd8570ac39dd61"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60ca5790f7d7a22db4e5f4fb492dbe22eb44"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60caa8a63f696dfa28dd109a44575b51d0e0"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60cab436636ab3fb6951d8c1ca638ac75dde"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60ca45d90c8af1a44579e7cf4024f3d9087d"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60ca148f57dd21fc83bf5db7786fff3ab1d7"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60cad194e370f95f67ec36eb973803594422"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60cad893cf892f7349e680b856f9c7bf7384"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60cafe7b5948cfc315eadfd2402bac9ae6a6"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60cafb77d719424231f9f7922de11754275c"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60ca2a88759e3ac3ef2e85552999df0589ae"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60ca492f5094e83bbb087de941a27801643f"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60cafc7a32ab0f21bf055a6ae3c4f7946d0c"></a>
<a id="gga37baf31388784ee8bcd4204a9520b60ca89fd9b164a9fad51545dbce7bb4fc3f8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__max2221x__interface_html_gaa1ed035adbbe144a7637a86011d9e88c"></a>
<a id="agroup__max2221x__interface_html_gga399738e28a4b7c309137d674e433ccb6aae654309f343b46f117327afe025c789"></a>
<a id="amisc_2max2221x_2max2221x_8h_html"></a>
<a id="aprintk_8h_html_a1bce54a738ce2d9dd6d95ee842ec237c"></a>
<a id="agroup__max2221x__interface_html_gaf3669424679108bafd9cf6ec9fdff1d1"></a>
<a id="agroup__max2221x__interface_html_gga2e92402dac3bd8036d0f1eff3e546c62ac69bf198154fd6084bdc981e1337b063"></a>
<a id="agroup__max2221x__interface_html_ga5a68165e4f5fbb0e6934572cd881889a"></a>
<a id="agroup__max2221x__interface_html_ggaef62d32791c1393a527bb26f7a42173fa3df216e71e2e032db275a892de63de7c"></a>
<a id="agroup__max2221x__interface_html_ga2a553f33ccbea8780cd5aa6e8259b14d"></a>
<a id="agroup__max2221x__interface_html_gga064959a318df5a214758a95bc11ae8eda5727a7f4e76cb429be734014a48790c8"></a>
<a id="agroup__max2221x__interface_html_ga5794ef47813b578767bf8d22c817bfc5"></a>
<a id="agroup__max2221x__interface_html_gga8f702fe056959c707d495a5b49ec7647a1710af28d11faf44c423f2f771f02980"></a>
<a id="agroup__max2221x__interface_html_gab671df1d71393c7a83772aa90d525c38"></a>
<a id="agroup__max2221x__interface_html_ggac3d8284e33a2cbc88e6e08396f6a2a66a6daf654eb4baaa6a59215fef63913a29"></a>
<a id="agroup__max2221x__interface_html_ga4c7ad2ac6af19be09ac4efef35fc9c60"></a>
<a id="agroup__max2221x__interface_html_gga5992183c2872bcf60726fb32784099c8a0cc4a45f17522eb715f9a515af2edd76"></a>
<a id="agroup__max2221x__interface_html_ga0de71917ab9598525fce343c2b451edf"></a>
<a id="agroup__max2221x__interface_html_ggafced3b909c7963f0711bb23eecb4b538a0eb8adae84e34d4bec22326d14ecfabc"></a>
<a id="agroup__max2221x__interface_html_ga8d417bccd2b1f015c8b985d0f8e64a41"></a>
<a id="agroup__max2221x__interface_html_gga37baf31388784ee8bcd4204a9520b60cae739f6bd1a1d4278a307ea35a0403f89"></a>
<a id="agroup__max2221x__interface_html_ga739a217f8e2e3518ca7223a05ea27f71"></a>
<a id="agroup__max2221x__interface_html_ga6255d9e0310281eccfacad971987a327"></a>
<a id="agroup__max2221x__interface_html_ga8e767d8da3317ca745c956a3758e4f1b"></a>
<a id="agroup__max2221x__interface_html_gaa8a88aebc1d8c5d8290514b540574c28"></a>
<a id="agroup__max2221x__interface_html_gaaed34f21363e832ff1db043a990c4c31"></a>
<a id="agroup__max2221x__interface_html_gae0c2320ed0790377ad1b3390a060db49"></a>
<a id="agroup__max2221x__interface_html_ga44a628faff5a7bdd9117a272db2bf76b"></a>

---

[上一章](P003_LTC4286 API主题.md) · [返回大纲](大纲.md) · [下一章](P005_应用网络上下文（Application network context）.md)
