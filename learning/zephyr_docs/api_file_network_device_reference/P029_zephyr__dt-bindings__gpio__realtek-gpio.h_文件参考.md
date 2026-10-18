---
id: learning.zephyr-docs.api-file-network-device-reference.page-29
title: zephyr__dt-bindings__gpio__realtek-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/realtek-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_dt-bindings\_\_gpio\_\_realtek-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/realtek-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 29.1\_宏定义（Macros）

<a id="r_ae59327ac268671ea2e20014f17701529"></a>

```c
#define RTS5912_GPIO_INDETEN BIT(8)
```

相关声明：[RTS5912_GPIO_INDETEN](#ae59327ac268671ea2e20014f17701529)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启用输入检测（Input Detect）。

<a id="r_a9f3289747c68c46fa5d8f92ebe0e2283"></a>

```c
#define RTS5912_GPIO_OUTDRV BIT(9)
```

相关声明：[RTS5912_GPIO_OUTDRV](#a9f3289747c68c46fa5d8f92ebe0e2283)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设置引脚驱动电流（Pin Driving Current）。

<a id="r_aa5af355318f8b6a034b85ed418de6cdd"></a>

```c
#define RTS5912_GPIO_SLEWRATE BIT(10)
```

相关声明：[RTS5912_GPIO_SLEWRATE](#aa5af355318f8b6a034b85ed418de6cdd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设置 GPIO 转换速率（Slew Rate）。

<a id="r_ae65d41879bcb126213ac007808086cee"></a>

```c
#define RTS5912_GPIO_SCHEN BIT(11)
```

相关声明：[RTS5912_GPIO_SCHEN](#ae65d41879bcb126213ac007808086cee)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启用施密特触发器（Schmitt Trigger）。

<a id="r_a0381dff71143b0fadceaaade950340a3"></a>

```c
#define RTS5912_GPIO_VOLTAGE_POS 12
```

相关声明：[RTS5912_GPIO_VOLTAGE_POS](#a0381dff71143b0fadceaaade950340a3)。

<a id="r_a9ab90e903840aec5172596492f12e6b5"></a>

```c
#define RTS5912_GPIO_VOLTAGE_MASK GENMASK(13, 12)
```

相关声明：[RTS5912_GPIO_VOLTAGE_MASK](#a9ab90e903840aec5172596492f12e6b5)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a91e7d587b96806b3f8403d3532d5a888"></a>

```c
#define RTS5912_GPIO_VOLTAGE_DEFAULT (0U << RTS5912_GPIO_VOLTAGE_POS)
```

相关声明：[RTS5912_GPIO_VOLTAGE_DEFAULT](#a91e7d587b96806b3f8403d3532d5a888)、[RTS5912_GPIO_VOLTAGE_POS](#a0381dff71143b0fadceaaade950340a3)。

将引脚设置为默认电压电平（Default Voltage Level）。

<a id="r_a83d8d0f0a827e770de9fe360fe566573"></a>

```c
#define RTS5912_GPIO_VOLTAGE_1V8 (1U << RTS5912_GPIO_VOLTAGE_POS)
```

相关声明：[RTS5912_GPIO_VOLTAGE_1V8](#a83d8d0f0a827e770de9fe360fe566573)、[RTS5912_GPIO_VOLTAGE_POS](#a0381dff71143b0fadceaaade950340a3)。

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

<a id="r_a24268d0667f7a2266e519c03e6a04395"></a>

```c
#define RTS5912_GPIO_VOLTAGE_3V3 (2U << RTS5912_GPIO_VOLTAGE_POS)
```

相关声明：[RTS5912_GPIO_VOLTAGE_3V3](#a24268d0667f7a2266e519c03e6a04395)、[RTS5912_GPIO_VOLTAGE_POS](#a0381dff71143b0fadceaaade950340a3)。

将引脚电压电平（Pin Voltage Level）设置为 3.3 V。

<a id="r_a0ca327e5b979185b539f187eabcbc0be"></a>

```c
#define RTS5912_GPIO_VOLTAGE_5V0 (3U << RTS5912_GPIO_VOLTAGE_POS)
```

相关声明：[RTS5912_GPIO_VOLTAGE_5V0](#a0ca327e5b979185b539f187eabcbc0be)、[RTS5912_GPIO_VOLTAGE_POS](#a0381dff71143b0fadceaaade950340a3)。

将引脚电压电平（Pin Voltage Level）设置为 5.0 V。

<a id="r_acea96124332b298d7f413105ed2c430f"></a>

```c
#define RTS5912_GPIO_MFCTRL_POS 14
```

相关声明：[RTS5912_GPIO_MFCTRL_POS](#acea96124332b298d7f413105ed2c430f)。

多功能（Multi Function）。

<a id="r_a661de5a3eb9f6b97f44735718c29dc43"></a>

```c
#define RTS5912_GPIO_MFCTRL_MASK GENMASK(15, 14)
```

相关声明：[RTS5912_GPIO_MFCTRL_MASK](#a661de5a3eb9f6b97f44735718c29dc43)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a93faaacf50a46b2209231e7eae2da8b4"></a>

```c
#define RTS5912_GPIO_MFCTRL_0 (0U << RTS5912_GPIO_MFCTRL_POS)
```

相关声明：[RTS5912_GPIO_MFCTRL_0](#a93faaacf50a46b2209231e7eae2da8b4)、[RTS5912_GPIO_MFCTRL_POS](#acea96124332b298d7f413105ed2c430f)。

`0x00`：功能 0；`0x01`：功能 1；`0x02`：功能 2；`0x03`：功能 3（Function 0–3）。

<a id="r_adf7208d3ffb32ee5f1d65deff41aaa74"></a>

```c
#define RTS5912_GPIO_MFCTRL_1 (1U << RTS5912_GPIO_MFCTRL_POS)
```

相关声明：[RTS5912_GPIO_MFCTRL_1](#adf7208d3ffb32ee5f1d65deff41aaa74)、[RTS5912_GPIO_MFCTRL_POS](#acea96124332b298d7f413105ed2c430f)。

<a id="r_ae492ac80b7741521601d6885d2f1b530"></a>

```c
#define RTS5912_GPIO_MFCTRL_2 (2U << RTS5912_GPIO_MFCTRL_POS)
```

相关声明：[RTS5912_GPIO_MFCTRL_2](#ae492ac80b7741521601d6885d2f1b530)、[RTS5912_GPIO_MFCTRL_POS](#acea96124332b298d7f413105ed2c430f)。

<a id="r_abf987c5c5f861c3d2ff57c664264acd0"></a>

```c
#define RTS5912_GPIO_MFCTRL_3 (3U << RTS5912_GPIO_MFCTRL_POS)
```

相关声明：[RTS5912_GPIO_MFCTRL_3](#abf987c5c5f861c3d2ff57c664264acd0)、[RTS5912_GPIO_MFCTRL_POS](#acea96124332b298d7f413105ed2c430f)。

<a id="r_a471603d5ffb1be381681a56d19b54757"></a>

```c
#define RTS5912_GPIO_INTR_MASK (1U << 21 | 1U << 22 | 1U << 24 | 1U << 25 | 1U << 26)
```

相关声明：[RTS5912_GPIO_INTR_MASK](#a471603d5ffb1be381681a56d19b54757)。

中断掩码（Interrupt Mask），因为 RTS5912 不支持 `GPIO_INT_LEVELS_LOGICAL`。

<a id="define-members-0"></a>

<a id="r_ae0f86929dec52d4e84ca76eac35a0f23"></a>

```c
#define RTS5912_GPIO000 &gpioa 0
```

相关声明：[RTS5912_GPIO000](#ae0f86929dec52d4e84ca76eac35a0f23)。

将 GPIO 信号名称映射到设备树绑定（Devicetree Binding）。

<a id="r_af17040023a6766a8679e4937e5b8741d"></a>

```c
#define RTS5912_GPIO001 &gpioa 1
```

相关声明：[RTS5912_GPIO001](#af17040023a6766a8679e4937e5b8741d)。

<a id="r_aea6a5befaec64e58fb96231492fcdcba"></a>

```c
#define RTS5912_GPIO002 &gpioa 2
```

相关声明：[RTS5912_GPIO002](#aea6a5befaec64e58fb96231492fcdcba)。

<a id="r_aa4767f0fe14db4c5ef2666a60843bf80"></a>

```c
#define RTS5912_GPIO003 &gpioa 3
```

相关声明：[RTS5912_GPIO003](#aa4767f0fe14db4c5ef2666a60843bf80)。

<a id="r_a384860bd17e836bf5edf599e3a9c44e8"></a>

```c
#define RTS5912_GPIO004 &gpioa 4
```

相关声明：[RTS5912_GPIO004](#a384860bd17e836bf5edf599e3a9c44e8)。

<a id="r_a3d19b2e45b4bffbe711b0fc514691d6a"></a>

```c
#define RTS5912_GPIO009 &gpioa 9
```

相关声明：[RTS5912_GPIO009](#a3d19b2e45b4bffbe711b0fc514691d6a)。

<a id="r_aa800db74134eb28a042566f6b8c774c5"></a>

```c
#define RTS5912_GPIO013 &gpioa 13
```

相关声明：[RTS5912_GPIO013](#aa800db74134eb28a042566f6b8c774c5)。

<a id="r_a3ec373be99a4e6ca2839e2b344bd5a57"></a>

```c
#define RTS5912_GPIO014 &gpioa 14
```

相关声明：[RTS5912_GPIO014](#a3ec373be99a4e6ca2839e2b344bd5a57)。

<a id="r_a718804d47a6ac0eb41af5d1c6533b3fc"></a>

```c
#define RTS5912_GPIO015 &gpioa 15
```

相关声明：[RTS5912_GPIO015](#a718804d47a6ac0eb41af5d1c6533b3fc)。

<a id="r_a1849b365332de65b0fede31d082eba7d"></a>

```c
#define RTS5912_GPIO016 &gpiob 0
```

相关声明：[RTS5912_GPIO016](#a1849b365332de65b0fede31d082eba7d)。

<a id="r_a66f428dade78b446f0c75b7226b6b349"></a>

```c
#define RTS5912_GPIO017 &gpiob 1
```

相关声明：[RTS5912_GPIO017](#a66f428dade78b446f0c75b7226b6b349)。

<a id="r_a42f889c5a43193fbd44b2c519d481366"></a>

```c
#define RTS5912_GPIO018 &gpiob 2
```

相关声明：[RTS5912_GPIO018](#a42f889c5a43193fbd44b2c519d481366)。

<a id="r_ad1b013e1a890059c61d0d7b78ad163df"></a>

```c
#define RTS5912_GPIO019 &gpiob 3
```

相关声明：[RTS5912_GPIO019](#ad1b013e1a890059c61d0d7b78ad163df)。

<a id="r_a8511a4d149aa415ae34e10ffd58c8860"></a>

```c
#define RTS5912_GPIO020 &gpiob 4
```

相关声明：[RTS5912_GPIO020](#a8511a4d149aa415ae34e10ffd58c8860)。

<a id="r_af2e02a6561f9a78709d6793a3765a190"></a>

```c
#define RTS5912_GPIO021 &gpiob 5
```

相关声明：[RTS5912_GPIO021](#af2e02a6561f9a78709d6793a3765a190)。

<a id="r_aee9f4947282e01ae703f09849a76446f"></a>

```c
#define RTS5912_GPIO022 &gpiob 6
```

相关声明：[RTS5912_GPIO022](#aee9f4947282e01ae703f09849a76446f)。

<a id="r_a8096f55ded538f9f49b38a56defaf455"></a>

```c
#define RTS5912_GPIO023 &gpiob 7
```

相关声明：[RTS5912_GPIO023](#a8096f55ded538f9f49b38a56defaf455)。

<a id="r_ac5159a17c6928307094093b9e8fbe82c"></a>

```c
#define RTS5912_GPIO025 &gpiob 9
```

相关声明：[RTS5912_GPIO025](#ac5159a17c6928307094093b9e8fbe82c)。

<a id="r_adefb134b4d9af7a160d8c267946813c1"></a>

```c
#define RTS5912_GPIO026 &gpiob 10
```

相关声明：[RTS5912_GPIO026](#adefb134b4d9af7a160d8c267946813c1)。

<a id="r_a0b18c525f8bf185740ddd7a531c36b3b"></a>

```c
#define RTS5912_GPIO027 &gpiob 11
```

相关声明：[RTS5912_GPIO027](#a0b18c525f8bf185740ddd7a531c36b3b)。

<a id="r_a08b8c566437bd77ce92473cb285e913a"></a>

```c
#define RTS5912_GPIO028 &gpiob 12
```

相关声明：[RTS5912_GPIO028](#a08b8c566437bd77ce92473cb285e913a)。

<a id="r_ac7efce949c05c079c1ec97ccb4848ed1"></a>

```c
#define RTS5912_GPIO029 &gpiob 13
```

相关声明：[RTS5912_GPIO029](#ac7efce949c05c079c1ec97ccb4848ed1)。

<a id="r_ad77384476fecfc236075c06c5c2ae6e5"></a>

```c
#define RTS5912_GPIO030 &gpiob 14
```

相关声明：[RTS5912_GPIO030](#ad77384476fecfc236075c06c5c2ae6e5)。

<a id="r_a30d53427a61729f8a4c63a490f8130b0"></a>

```c
#define RTS5912_GPIO031 &gpiob 15
```

相关声明：[RTS5912_GPIO031](#a30d53427a61729f8a4c63a490f8130b0)。

<a id="r_a3bc66b1b9cc36eae0bf490497dc09ece"></a>

```c
#define RTS5912_GPIO040 &gpioc 8
```

相关声明：[RTS5912_GPIO040](#a3bc66b1b9cc36eae0bf490497dc09ece)。

<a id="r_a990d780d473b26776375db97d3b909ab"></a>

```c
#define RTS5912_GPIO041 &gpioc 9
```

相关声明：[RTS5912_GPIO041](#a990d780d473b26776375db97d3b909ab)。

<a id="r_a90c07deda1fbc4a504a25c43324977df"></a>

```c
#define RTS5912_GPIO042 &gpioc 10
```

相关声明：[RTS5912_GPIO042](#a90c07deda1fbc4a504a25c43324977df)。

<a id="r_abfc7ad5e026d99cb0bd9a0f8b693e4c1"></a>

```c
#define RTS5912_GPIO043 &gpioc 11
```

相关声明：[RTS5912_GPIO043](#abfc7ad5e026d99cb0bd9a0f8b693e4c1)。

<a id="r_acb77f8465e449807e67f787bb629ea38"></a>

```c
#define RTS5912_GPIO044 &gpioc 12
```

相关声明：[RTS5912_GPIO044](#acb77f8465e449807e67f787bb629ea38)。

<a id="r_a419ebe4e5acc77b6244ebaf76577dc7f"></a>

```c
#define RTS5912_GPIO045 &gpioc 13
```

相关声明：[RTS5912_GPIO045](#a419ebe4e5acc77b6244ebaf76577dc7f)。

<a id="r_aa6a5b3324ac34603db61727f84de53ed"></a>

```c
#define RTS5912_GPIO046 &gpioc 14
```

相关声明：[RTS5912_GPIO046](#aa6a5b3324ac34603db61727f84de53ed)。

<a id="r_a9cf5fa59a7c3414da2d5595b390007fd"></a>

```c
#define RTS5912_GPIO047 &gpioc 15
```

相关声明：[RTS5912_GPIO047](#a9cf5fa59a7c3414da2d5595b390007fd)。

<a id="r_a089b3b5dec91d100216bc7bbc8dbc768"></a>

```c
#define RTS5912_GPIO048 &gpiod 0
```

相关声明：[RTS5912_GPIO048](#a089b3b5dec91d100216bc7bbc8dbc768)。

<a id="r_a17ae41a7b07060748114ba9054e7b1dc"></a>

```c
#define RTS5912_GPIO049 &gpiod 1
```

相关声明：[RTS5912_GPIO049](#a17ae41a7b07060748114ba9054e7b1dc)。

<a id="r_af4829cf2e0c1d0d377d6c97e62d4a792"></a>

```c
#define RTS5912_GPIO050 &gpiod 2
```

相关声明：[RTS5912_GPIO050](#af4829cf2e0c1d0d377d6c97e62d4a792)。

<a id="r_ab6b380ed252878d6f3fd84ac569c156d"></a>

```c
#define RTS5912_GPIO051 &gpiod 3
```

相关声明：[RTS5912_GPIO051](#ab6b380ed252878d6f3fd84ac569c156d)。

<a id="r_acd1ef6193ed72c4d12dc4d54fe76baae"></a>

```c
#define RTS5912_GPIO052 &gpiod 4
```

相关声明：[RTS5912_GPIO052](#acd1ef6193ed72c4d12dc4d54fe76baae)。

<a id="r_a9cde17bb6e574910d154f1ec9d35b09e"></a>

```c
#define RTS5912_GPIO053 &gpiod 5
```

相关声明：[RTS5912_GPIO053](#a9cde17bb6e574910d154f1ec9d35b09e)。

<a id="r_a5ae5cc06b3af144cc33a3aec2d6cbfc6"></a>

```c
#define RTS5912_GPIO055 &gpiod 7
```

相关声明：[RTS5912_GPIO055](#a5ae5cc06b3af144cc33a3aec2d6cbfc6)。

<a id="r_a330300eb8c9b29f3bb6542f62e467877"></a>

```c
#define RTS5912_GPIO056 &gpiod 8
```

相关声明：[RTS5912_GPIO056](#a330300eb8c9b29f3bb6542f62e467877)。

<a id="r_a17980817323f360602860ae592bda32d"></a>

```c
#define RTS5912_GPIO057 &gpiod 9
```

相关声明：[RTS5912_GPIO057](#a17980817323f360602860ae592bda32d)。

<a id="r_a7ce0f552341ff7c7dacd28b04cf83866"></a>

```c
#define RTS5912_GPIO058 &gpiod 10
```

相关声明：[RTS5912_GPIO058](#a7ce0f552341ff7c7dacd28b04cf83866)。

<a id="r_abf5a87bc0d1f5756e3e92bc1265d2147"></a>

```c
#define RTS5912_GPIO059 &gpiod 11
```

相关声明：[RTS5912_GPIO059](#abf5a87bc0d1f5756e3e92bc1265d2147)。

<a id="r_a2bd7947fc48c3b591666e66da8cfd426"></a>

```c
#define RTS5912_GPIO060 &gpiod 12
```

相关声明：[RTS5912_GPIO060](#a2bd7947fc48c3b591666e66da8cfd426)。

<a id="r_a79afed7ce7a0577d518577b54c0b0646"></a>

```c
#define RTS5912_GPIO061 &gpiod 13
```

相关声明：[RTS5912_GPIO061](#a79afed7ce7a0577d518577b54c0b0646)。

<a id="r_a8dbde266e97c670f3fb4d9ceacadd390"></a>

```c
#define RTS5912_GPIO064 &gpioe 0
```

相关声明：[RTS5912_GPIO064](#a8dbde266e97c670f3fb4d9ceacadd390)。

<a id="r_ae8722022ad634c9a18db2a720723f8e8"></a>

```c
#define RTS5912_GPIO065 &gpioe 1
```

相关声明：[RTS5912_GPIO065](#ae8722022ad634c9a18db2a720723f8e8)。

<a id="r_a5bbcabed6d4f62e91b39bcd2fdc63e88"></a>

```c
#define RTS5912_GPIO066 &gpioe 2
```

相关声明：[RTS5912_GPIO066](#a5bbcabed6d4f62e91b39bcd2fdc63e88)。

<a id="r_ab7ec6c21c3247d34665b2f71ec381e88"></a>

```c
#define RTS5912_GPIO067 &gpioe 3
```

相关声明：[RTS5912_GPIO067](#ab7ec6c21c3247d34665b2f71ec381e88)。

<a id="r_a82ff10e0a6941308308370ae5c9747ed"></a>

```c
#define RTS5912_GPIO068 &gpioe 4
```

相关声明：[RTS5912_GPIO068](#a82ff10e0a6941308308370ae5c9747ed)。

<a id="r_a31ec5c35fd46495d9fa31a4672058840"></a>

```c
#define RTS5912_GPIO069 &gpioe 5
```

相关声明：[RTS5912_GPIO069](#a31ec5c35fd46495d9fa31a4672058840)。

<a id="r_a713f1b256dbafb5ee84d4680ffa6773d"></a>

```c
#define RTS5912_GPIO070 &gpioe 6
```

相关声明：[RTS5912_GPIO070](#a713f1b256dbafb5ee84d4680ffa6773d)。

<a id="r_aad6e5e13a6a6fb4a559ed37ff41d91d6"></a>

```c
#define RTS5912_GPIO071 &gpioe 7
```

相关声明：[RTS5912_GPIO071](#aad6e5e13a6a6fb4a559ed37ff41d91d6)。

<a id="r_ae375ba9f3e40378761bda6b5276fc83e"></a>

```c
#define RTS5912_GPIO074 &gpioe 10
```

相关声明：[RTS5912_GPIO074](#ae375ba9f3e40378761bda6b5276fc83e)。

<a id="r_a66376bc76dbfc2fdc44071e1ab8eadd5"></a>

```c
#define RTS5912_GPIO075 &gpioe 11
```

相关声明：[RTS5912_GPIO075](#a66376bc76dbfc2fdc44071e1ab8eadd5)。

<a id="r_a2b0797a5e786b5e10c2df44f15b7bda7"></a>

```c
#define RTS5912_GPIO076 &gpioe 12
```

相关声明：[RTS5912_GPIO076](#a2b0797a5e786b5e10c2df44f15b7bda7)。

<a id="r_a9660ec85627d04c149246fbdc5ed82c1"></a>

```c
#define RTS5912_GPIO077 &gpioe 13
```

相关声明：[RTS5912_GPIO077](#a9660ec85627d04c149246fbdc5ed82c1)。

<a id="r_abbab6c292bfa4ebb1b6898556b7e6ef3"></a>

```c
#define RTS5912_GPIO078 &gpioe 14
```

相关声明：[RTS5912_GPIO078](#abbab6c292bfa4ebb1b6898556b7e6ef3)。

<a id="r_acc05c3d94e0d166e45a9a04321e0c8c2"></a>

```c
#define RTS5912_GPIO079 &gpioe 15
```

相关声明：[RTS5912_GPIO079](#acc05c3d94e0d166e45a9a04321e0c8c2)。

<a id="r_a542642fbaa3ee10f7abbe6bafccba4cf"></a>

```c
#define RTS5912_GPIO080 &gpiof 0
```

相关声明：[RTS5912_GPIO080](#a542642fbaa3ee10f7abbe6bafccba4cf)。

<a id="r_a76b86c281afd6b25394c85aeff908a13"></a>

```c
#define RTS5912_GPIO081 &gpiof 1
```

相关声明：[RTS5912_GPIO081](#a76b86c281afd6b25394c85aeff908a13)。

<a id="r_a9e90e0c340288c3f9c0742175ec74571"></a>

```c
#define RTS5912_GPIO083 &gpiof 3
```

相关声明：[RTS5912_GPIO083](#a9e90e0c340288c3f9c0742175ec74571)。

<a id="r_ad89d02dac166125415dba9e9876d60be"></a>

```c
#define RTS5912_GPIO084 &gpiof 4
```

相关声明：[RTS5912_GPIO084](#ad89d02dac166125415dba9e9876d60be)。

<a id="r_a907b005215a07ab421c473c7a3dc6fb2"></a>

```c
#define RTS5912_GPIO085 &gpiof 5
```

相关声明：[RTS5912_GPIO085](#a907b005215a07ab421c473c7a3dc6fb2)。

<a id="r_a14b3decaebaea14b861fb7a9079c7000"></a>

```c
#define RTS5912_GPIO086 &gpiof 6
```

相关声明：[RTS5912_GPIO086](#a14b3decaebaea14b861fb7a9079c7000)。

<a id="r_aab89a3c0cbf8ee9c5812e1c46b12d0e5"></a>

```c
#define RTS5912_GPIO087 &gpiof 7
```

相关声明：[RTS5912_GPIO087](#aab89a3c0cbf8ee9c5812e1c46b12d0e5)。

<a id="r_adbc22009dbd6cced0d61f6e346e9d011"></a>

```c
#define RTS5912_GPIO088 &gpiof 8
```

相关声明：[RTS5912_GPIO088](#adbc22009dbd6cced0d61f6e346e9d011)。

<a id="r_ac2aad29217d78204e687a2f310e30991"></a>

```c
#define RTS5912_GPIO089 &gpiof 9
```

相关声明：[RTS5912_GPIO089](#ac2aad29217d78204e687a2f310e30991)。

<a id="r_a2fa7308395350cd605df774bbf23d854"></a>

```c
#define RTS5912_GPIO090 &gpiof 10
```

相关声明：[RTS5912_GPIO090](#a2fa7308395350cd605df774bbf23d854)。

<a id="r_a24df43c66502171355617248507cdec3"></a>

```c
#define RTS5912_GPIO091 &gpiof 11
```

相关声明：[RTS5912_GPIO091](#a24df43c66502171355617248507cdec3)。

<a id="r_a8799387ece3ebbe0813ab5788d516404"></a>

```c
#define RTS5912_GPIO092 &gpiof 12
```

相关声明：[RTS5912_GPIO092](#a8799387ece3ebbe0813ab5788d516404)。

<a id="r_af07451f8208714af711cd81e8e8257f8"></a>

```c
#define RTS5912_GPIO093 &gpiof 13
```

相关声明：[RTS5912_GPIO093](#af07451f8208714af711cd81e8e8257f8)。

<a id="r_a9549c09d7c14024ab1a9dfeb27a431a9"></a>

```c
#define RTS5912_GPIO094 &gpiof 14
```

相关声明：[RTS5912_GPIO094](#a9549c09d7c14024ab1a9dfeb27a431a9)。

<a id="r_ab109503f090349dc2d4deec7eb8dfce8"></a>

```c
#define RTS5912_GPIO095 &gpiof 15
```

相关声明：[RTS5912_GPIO095](#ab109503f090349dc2d4deec7eb8dfce8)。

<a id="r_a7ab160b69297a6e96b13454715e94e23"></a>

```c
#define RTS5912_GPIO096 &gpiog 0
```

相关声明：[RTS5912_GPIO096](#a7ab160b69297a6e96b13454715e94e23)。

<a id="r_a2e5788350850a02a9ba950f2f43ccd28"></a>

```c
#define RTS5912_GPIO097 &gpiog 1
```

相关声明：[RTS5912_GPIO097](#a2e5788350850a02a9ba950f2f43ccd28)。

<a id="r_a636df55246c056b02dba78a9e90f7955"></a>

```c
#define RTS5912_GPIO099 &gpiog 3
```

相关声明：[RTS5912_GPIO099](#a636df55246c056b02dba78a9e90f7955)。

<a id="r_a1d0870f2c0b4c60fe027c0c89f6337df"></a>

```c
#define RTS5912_GPIO100 &gpiog 4
```

相关声明：[RTS5912_GPIO100](#a1d0870f2c0b4c60fe027c0c89f6337df)。

<a id="r_adeb294d938585973841b8621c21c6b65"></a>

```c
#define RTS5912_GPIO101 &gpiog 5
```

相关声明：[RTS5912_GPIO101](#adeb294d938585973841b8621c21c6b65)。

<a id="r_a3fba435e70009cecb5b47c5fe9da7902"></a>

```c
#define RTS5912_GPIO102 &gpiog 6
```

相关声明：[RTS5912_GPIO102](#a3fba435e70009cecb5b47c5fe9da7902)。

<a id="r_a5fc5b83b06b807d7abf2b57c96e891f5"></a>

```c
#define RTS5912_GPIO103 &gpiog 7
```

相关声明：[RTS5912_GPIO103](#a5fc5b83b06b807d7abf2b57c96e891f5)。

<a id="r_a003e66685e2bb853e22026ee20c9f32e"></a>

```c
#define RTS5912_GPIO104 &gpiog 8
```

相关声明：[RTS5912_GPIO104](#a003e66685e2bb853e22026ee20c9f32e)。

<a id="r_a8129b0863a2d5bdcbe68be9d867ba6f9"></a>

```c
#define RTS5912_GPIO105 &gpiog 9
```

相关声明：[RTS5912_GPIO105](#a8129b0863a2d5bdcbe68be9d867ba6f9)。

<a id="r_a6f455cb1dea82764502381e47355ddc0"></a>

```c
#define RTS5912_GPIO106 &gpiog 10
```

相关声明：[RTS5912_GPIO106](#a6f455cb1dea82764502381e47355ddc0)。

<a id="r_a0a7b9479655fd826fab1f3b14e5b0b77"></a>

```c
#define RTS5912_GPIO107 &gpiog 11
```

相关声明：[RTS5912_GPIO107](#a0a7b9479655fd826fab1f3b14e5b0b77)。

<a id="r_a3b4910c5ff979f29d2565313862c4ea9"></a>

```c
#define RTS5912_GPIO108 &gpiog 12
```

相关声明：[RTS5912_GPIO108](#a3b4910c5ff979f29d2565313862c4ea9)。

<a id="r_a9cd237a023d2c74c2d58c30a90771521"></a>

```c
#define RTS5912_GPIO109 &gpiog 13
```

相关声明：[RTS5912_GPIO109](#a9cd237a023d2c74c2d58c30a90771521)。

<a id="r_a1ed72627549ba6a83e2354845fa2d4a3"></a>

```c
#define RTS5912_GPIO111 &gpiog 15
```

相关声明：[RTS5912_GPIO111](#a1ed72627549ba6a83e2354845fa2d4a3)。

<a id="r_a24607480aae6f79e2ef88a231b15cead"></a>

```c
#define RTS5912_GPIO112 &gpioh 0
```

相关声明：[RTS5912_GPIO112](#a24607480aae6f79e2ef88a231b15cead)。

<a id="r_aee14981a7bf40b01892b73422ecb1430"></a>

```c
#define RTS5912_GPIO113 &gpioh 1
```

相关声明：[RTS5912_GPIO113](#aee14981a7bf40b01892b73422ecb1430)。

<a id="r_abda47f90d482d3cfe2055f4168096c25"></a>

```c
#define RTS5912_GPIO114 &gpioh 2
```

相关声明：[RTS5912_GPIO114](#abda47f90d482d3cfe2055f4168096c25)。

<a id="r_a16a02bdb746fddfb6956cb9a286678d6"></a>

```c
#define RTS5912_GPIO115 &gpioh 3
```

相关声明：[RTS5912_GPIO115](#a16a02bdb746fddfb6956cb9a286678d6)。

<a id="r_a9ee03b46798cab05c215e3536db77bfb"></a>

```c
#define RTS5912_GPIO117 &gpioh 5
```

相关声明：[RTS5912_GPIO117](#a9ee03b46798cab05c215e3536db77bfb)。

<a id="r_a2297d78143290ac827b4532bb71f94cc"></a>

```c
#define RTS5912_GPIO118 &gpioh 6
```

相关声明：[RTS5912_GPIO118](#a2297d78143290ac827b4532bb71f94cc)。

<a id="r_ad81fc0b32d6eeca09e58c80aae92d5bc"></a>

```c
#define RTS5912_GPIO119 &gpioh 7
```

相关声明：[RTS5912_GPIO119](#ad81fc0b32d6eeca09e58c80aae92d5bc)。

<a id="r_afc2ee390daa1e132d0638e780637e224"></a>

```c
#define RTS5912_GPIO120 &gpioh 8
```

相关声明：[RTS5912_GPIO120](#afc2ee390daa1e132d0638e780637e224)。

<a id="r_aed0d9cc26a90e7e7c687186494836adf"></a>

```c
#define RTS5912_GPIO121 &gpioh 9
```

相关声明：[RTS5912_GPIO121](#aed0d9cc26a90e7e7c687186494836adf)。

<a id="r_aec88be11094c0589773fa285032c9a56"></a>

```c
#define RTS5912_GPIO122 &gpioh 10
```

相关声明：[RTS5912_GPIO122](#aec88be11094c0589773fa285032c9a56)。

<a id="r_aabe0dc95aa117ee0c669827be4e97481"></a>

```c
#define RTS5912_GPIO123 &gpioh 11
```

相关声明：[RTS5912_GPIO123](#aabe0dc95aa117ee0c669827be4e97481)。

<a id="r_a8ae5b6fe831cab6aef485377453e8634"></a>

```c
#define RTS5912_GPIO124 &gpioh 12
```

相关声明：[RTS5912_GPIO124](#a8ae5b6fe831cab6aef485377453e8634)。

<a id="r_a2418255405a582a6d7974ffd995735fd"></a>

```c
#define RTS5912_GPIO125 &gpioh 13
```

相关声明：[RTS5912_GPIO125](#a2418255405a582a6d7974ffd995735fd)。

<a id="r_aad4ff9bb48086611f205c1b362b11881"></a>

```c
#define RTS5912_GPIO126 &gpioh 14
```

相关声明：[RTS5912_GPIO126](#aad4ff9bb48086611f205c1b362b11881)。

<a id="r_a7394601627c978cdcbcc46234878cb6c"></a>

```c
#define RTS5912_GPIO127 &gpioh 15
```

相关声明：[RTS5912_GPIO127](#a7394601627c978cdcbcc46234878cb6c)。

<a id="r_abeca8744b42ebe3f04594064f352187d"></a>

```c
#define RTS5912_GPIO128 &gpioi 0
```

相关声明：[RTS5912_GPIO128](#abeca8744b42ebe3f04594064f352187d)。

<a id="r_afc4124ad28042361d67ed609dfcf0da7"></a>

```c
#define RTS5912_GPIO130 &gpioi 2
```

相关声明：[RTS5912_GPIO130](#afc4124ad28042361d67ed609dfcf0da7)。

<a id="r_ada607c13918188d3f629363d143ea6cf"></a>

```c
#define RTS5912_GPIO131 &gpioi 3
```

相关声明：[RTS5912_GPIO131](#ada607c13918188d3f629363d143ea6cf)。

## 29.2\_详细说明（Detailed Documentation）

<a id="ae0f86929dec52d4e84ca76eac35a0f23"></a>

### `RTS5912_GPIO000`

```c
#define RTS5912_GPIO000 &gpioa 0
```

将 GPIO 信号名称映射到设备树绑定（Devicetree Binding）。

RTS5912 文档采用八进制 GPIO 引脚编号（Octal Pin Numbering）；使用这些宏时，用户无需自行进行 GPIO 编号转换。

设备树用法示例（Example DT Usage）：

原始示例（Example）：

```c
gpios = <RTS5912_GPIO102 (GPIO_OUTPUT)>;
```

<a id="af17040023a6766a8679e4937e5b8741d"></a>

### `RTS5912_GPIO001`

```c
#define RTS5912_GPIO001 &gpioa 1
```

<a id="aea6a5befaec64e58fb96231492fcdcba"></a>

### `RTS5912_GPIO002`

```c
#define RTS5912_GPIO002 &gpioa 2
```

<a id="aa4767f0fe14db4c5ef2666a60843bf80"></a>

### `RTS5912_GPIO003`

```c
#define RTS5912_GPIO003 &gpioa 3
```

<a id="a384860bd17e836bf5edf599e3a9c44e8"></a>

### `RTS5912_GPIO004`

```c
#define RTS5912_GPIO004 &gpioa 4
```

<a id="a3d19b2e45b4bffbe711b0fc514691d6a"></a>

### `RTS5912_GPIO009`

```c
#define RTS5912_GPIO009 &gpioa 9
```

<a id="aa800db74134eb28a042566f6b8c774c5"></a>

### `RTS5912_GPIO013`

```c
#define RTS5912_GPIO013 &gpioa 13
```

<a id="a3ec373be99a4e6ca2839e2b344bd5a57"></a>

### `RTS5912_GPIO014`

```c
#define RTS5912_GPIO014 &gpioa 14
```

<a id="a718804d47a6ac0eb41af5d1c6533b3fc"></a>

### `RTS5912_GPIO015`

```c
#define RTS5912_GPIO015 &gpioa 15
```

<a id="a1849b365332de65b0fede31d082eba7d"></a>

### `RTS5912_GPIO016`

```c
#define RTS5912_GPIO016 &gpiob 0
```

<a id="a66f428dade78b446f0c75b7226b6b349"></a>

### `RTS5912_GPIO017`

```c
#define RTS5912_GPIO017 &gpiob 1
```

<a id="a42f889c5a43193fbd44b2c519d481366"></a>

### `RTS5912_GPIO018`

```c
#define RTS5912_GPIO018 &gpiob 2
```

<a id="ad1b013e1a890059c61d0d7b78ad163df"></a>

### `RTS5912_GPIO019`

```c
#define RTS5912_GPIO019 &gpiob 3
```

<a id="a8511a4d149aa415ae34e10ffd58c8860"></a>

### `RTS5912_GPIO020`

```c
#define RTS5912_GPIO020 &gpiob 4
```

<a id="af2e02a6561f9a78709d6793a3765a190"></a>

### `RTS5912_GPIO021`

```c
#define RTS5912_GPIO021 &gpiob 5
```

<a id="aee9f4947282e01ae703f09849a76446f"></a>

### `RTS5912_GPIO022`

```c
#define RTS5912_GPIO022 &gpiob 6
```

<a id="a8096f55ded538f9f49b38a56defaf455"></a>

### `RTS5912_GPIO023`

```c
#define RTS5912_GPIO023 &gpiob 7
```

<a id="ac5159a17c6928307094093b9e8fbe82c"></a>

### `RTS5912_GPIO025`

```c
#define RTS5912_GPIO025 &gpiob 9
```

<a id="adefb134b4d9af7a160d8c267946813c1"></a>

### `RTS5912_GPIO026`

```c
#define RTS5912_GPIO026 &gpiob 10
```

<a id="a0b18c525f8bf185740ddd7a531c36b3b"></a>

### `RTS5912_GPIO027`

```c
#define RTS5912_GPIO027 &gpiob 11
```

<a id="a08b8c566437bd77ce92473cb285e913a"></a>

### `RTS5912_GPIO028`

```c
#define RTS5912_GPIO028 &gpiob 12
```

<a id="ac7efce949c05c079c1ec97ccb4848ed1"></a>

### `RTS5912_GPIO029`

```c
#define RTS5912_GPIO029 &gpiob 13
```

<a id="ad77384476fecfc236075c06c5c2ae6e5"></a>

### `RTS5912_GPIO030`

```c
#define RTS5912_GPIO030 &gpiob 14
```

<a id="a30d53427a61729f8a4c63a490f8130b0"></a>

### `RTS5912_GPIO031`

```c
#define RTS5912_GPIO031 &gpiob 15
```

<a id="a3bc66b1b9cc36eae0bf490497dc09ece"></a>

### `RTS5912_GPIO040`

```c
#define RTS5912_GPIO040 &gpioc 8
```

<a id="a990d780d473b26776375db97d3b909ab"></a>

### `RTS5912_GPIO041`

```c
#define RTS5912_GPIO041 &gpioc 9
```

<a id="a90c07deda1fbc4a504a25c43324977df"></a>

### `RTS5912_GPIO042`

```c
#define RTS5912_GPIO042 &gpioc 10
```

<a id="abfc7ad5e026d99cb0bd9a0f8b693e4c1"></a>

### `RTS5912_GPIO043`

```c
#define RTS5912_GPIO043 &gpioc 11
```

<a id="acb77f8465e449807e67f787bb629ea38"></a>

### `RTS5912_GPIO044`

```c
#define RTS5912_GPIO044 &gpioc 12
```

<a id="a419ebe4e5acc77b6244ebaf76577dc7f"></a>

### `RTS5912_GPIO045`

```c
#define RTS5912_GPIO045 &gpioc 13
```

<a id="aa6a5b3324ac34603db61727f84de53ed"></a>

### `RTS5912_GPIO046`

```c
#define RTS5912_GPIO046 &gpioc 14
```

<a id="a9cf5fa59a7c3414da2d5595b390007fd"></a>

### `RTS5912_GPIO047`

```c
#define RTS5912_GPIO047 &gpioc 15
```

<a id="a089b3b5dec91d100216bc7bbc8dbc768"></a>

### `RTS5912_GPIO048`

```c
#define RTS5912_GPIO048 &gpiod 0
```

<a id="a17ae41a7b07060748114ba9054e7b1dc"></a>

### `RTS5912_GPIO049`

```c
#define RTS5912_GPIO049 &gpiod 1
```

<a id="af4829cf2e0c1d0d377d6c97e62d4a792"></a>

### `RTS5912_GPIO050`

```c
#define RTS5912_GPIO050 &gpiod 2
```

<a id="ab6b380ed252878d6f3fd84ac569c156d"></a>

### `RTS5912_GPIO051`

```c
#define RTS5912_GPIO051 &gpiod 3
```

<a id="acd1ef6193ed72c4d12dc4d54fe76baae"></a>

### `RTS5912_GPIO052`

```c
#define RTS5912_GPIO052 &gpiod 4
```

<a id="a9cde17bb6e574910d154f1ec9d35b09e"></a>

### `RTS5912_GPIO053`

```c
#define RTS5912_GPIO053 &gpiod 5
```

<a id="a5ae5cc06b3af144cc33a3aec2d6cbfc6"></a>

### `RTS5912_GPIO055`

```c
#define RTS5912_GPIO055 &gpiod 7
```

<a id="a330300eb8c9b29f3bb6542f62e467877"></a>

### `RTS5912_GPIO056`

```c
#define RTS5912_GPIO056 &gpiod 8
```

<a id="a17980817323f360602860ae592bda32d"></a>

### `RTS5912_GPIO057`

```c
#define RTS5912_GPIO057 &gpiod 9
```

<a id="a7ce0f552341ff7c7dacd28b04cf83866"></a>

### `RTS5912_GPIO058`

```c
#define RTS5912_GPIO058 &gpiod 10
```

<a id="abf5a87bc0d1f5756e3e92bc1265d2147"></a>

### `RTS5912_GPIO059`

```c
#define RTS5912_GPIO059 &gpiod 11
```

<a id="a2bd7947fc48c3b591666e66da8cfd426"></a>

### `RTS5912_GPIO060`

```c
#define RTS5912_GPIO060 &gpiod 12
```

<a id="a79afed7ce7a0577d518577b54c0b0646"></a>

### `RTS5912_GPIO061`

```c
#define RTS5912_GPIO061 &gpiod 13
```

<a id="a8dbde266e97c670f3fb4d9ceacadd390"></a>

### `RTS5912_GPIO064`

```c
#define RTS5912_GPIO064 &gpioe 0
```

<a id="ae8722022ad634c9a18db2a720723f8e8"></a>

### `RTS5912_GPIO065`

```c
#define RTS5912_GPIO065 &gpioe 1
```

<a id="a5bbcabed6d4f62e91b39bcd2fdc63e88"></a>

### `RTS5912_GPIO066`

```c
#define RTS5912_GPIO066 &gpioe 2
```

<a id="ab7ec6c21c3247d34665b2f71ec381e88"></a>

### `RTS5912_GPIO067`

```c
#define RTS5912_GPIO067 &gpioe 3
```

<a id="a82ff10e0a6941308308370ae5c9747ed"></a>

### `RTS5912_GPIO068`

```c
#define RTS5912_GPIO068 &gpioe 4
```

<a id="a31ec5c35fd46495d9fa31a4672058840"></a>

### `RTS5912_GPIO069`

```c
#define RTS5912_GPIO069 &gpioe 5
```

<a id="a713f1b256dbafb5ee84d4680ffa6773d"></a>

### `RTS5912_GPIO070`

```c
#define RTS5912_GPIO070 &gpioe 6
```

<a id="aad6e5e13a6a6fb4a559ed37ff41d91d6"></a>

### `RTS5912_GPIO071`

```c
#define RTS5912_GPIO071 &gpioe 7
```

<a id="ae375ba9f3e40378761bda6b5276fc83e"></a>

### `RTS5912_GPIO074`

```c
#define RTS5912_GPIO074 &gpioe 10
```

<a id="a66376bc76dbfc2fdc44071e1ab8eadd5"></a>

### `RTS5912_GPIO075`

```c
#define RTS5912_GPIO075 &gpioe 11
```

<a id="a2b0797a5e786b5e10c2df44f15b7bda7"></a>

### `RTS5912_GPIO076`

```c
#define RTS5912_GPIO076 &gpioe 12
```

<a id="a9660ec85627d04c149246fbdc5ed82c1"></a>

### `RTS5912_GPIO077`

```c
#define RTS5912_GPIO077 &gpioe 13
```

<a id="abbab6c292bfa4ebb1b6898556b7e6ef3"></a>

### `RTS5912_GPIO078`

```c
#define RTS5912_GPIO078 &gpioe 14
```

<a id="acc05c3d94e0d166e45a9a04321e0c8c2"></a>

### `RTS5912_GPIO079`

```c
#define RTS5912_GPIO079 &gpioe 15
```

<a id="a542642fbaa3ee10f7abbe6bafccba4cf"></a>

### `RTS5912_GPIO080`

```c
#define RTS5912_GPIO080 &gpiof 0
```

<a id="a76b86c281afd6b25394c85aeff908a13"></a>

### `RTS5912_GPIO081`

```c
#define RTS5912_GPIO081 &gpiof 1
```

<a id="a9e90e0c340288c3f9c0742175ec74571"></a>

### `RTS5912_GPIO083`

```c
#define RTS5912_GPIO083 &gpiof 3
```

<a id="ad89d02dac166125415dba9e9876d60be"></a>

### `RTS5912_GPIO084`

```c
#define RTS5912_GPIO084 &gpiof 4
```

<a id="a907b005215a07ab421c473c7a3dc6fb2"></a>

### `RTS5912_GPIO085`

```c
#define RTS5912_GPIO085 &gpiof 5
```

<a id="a14b3decaebaea14b861fb7a9079c7000"></a>

### `RTS5912_GPIO086`

```c
#define RTS5912_GPIO086 &gpiof 6
```

<a id="aab89a3c0cbf8ee9c5812e1c46b12d0e5"></a>

### `RTS5912_GPIO087`

```c
#define RTS5912_GPIO087 &gpiof 7
```

<a id="adbc22009dbd6cced0d61f6e346e9d011"></a>

### `RTS5912_GPIO088`

```c
#define RTS5912_GPIO088 &gpiof 8
```

<a id="ac2aad29217d78204e687a2f310e30991"></a>

### `RTS5912_GPIO089`

```c
#define RTS5912_GPIO089 &gpiof 9
```

<a id="a2fa7308395350cd605df774bbf23d854"></a>

### `RTS5912_GPIO090`

```c
#define RTS5912_GPIO090 &gpiof 10
```

<a id="a24df43c66502171355617248507cdec3"></a>

### `RTS5912_GPIO091`

```c
#define RTS5912_GPIO091 &gpiof 11
```

<a id="a8799387ece3ebbe0813ab5788d516404"></a>

### `RTS5912_GPIO092`

```c
#define RTS5912_GPIO092 &gpiof 12
```

<a id="af07451f8208714af711cd81e8e8257f8"></a>

### `RTS5912_GPIO093`

```c
#define RTS5912_GPIO093 &gpiof 13
```

<a id="a9549c09d7c14024ab1a9dfeb27a431a9"></a>

### `RTS5912_GPIO094`

```c
#define RTS5912_GPIO094 &gpiof 14
```

<a id="ab109503f090349dc2d4deec7eb8dfce8"></a>

### `RTS5912_GPIO095`

```c
#define RTS5912_GPIO095 &gpiof 15
```

<a id="a7ab160b69297a6e96b13454715e94e23"></a>

### `RTS5912_GPIO096`

```c
#define RTS5912_GPIO096 &gpiog 0
```

<a id="a2e5788350850a02a9ba950f2f43ccd28"></a>

### `RTS5912_GPIO097`

```c
#define RTS5912_GPIO097 &gpiog 1
```

<a id="a636df55246c056b02dba78a9e90f7955"></a>

### `RTS5912_GPIO099`

```c
#define RTS5912_GPIO099 &gpiog 3
```

<a id="a1d0870f2c0b4c60fe027c0c89f6337df"></a>

### `RTS5912_GPIO100`

```c
#define RTS5912_GPIO100 &gpiog 4
```

<a id="adeb294d938585973841b8621c21c6b65"></a>

### `RTS5912_GPIO101`

```c
#define RTS5912_GPIO101 &gpiog 5
```

<a id="a3fba435e70009cecb5b47c5fe9da7902"></a>

### `RTS5912_GPIO102`

```c
#define RTS5912_GPIO102 &gpiog 6
```

<a id="a5fc5b83b06b807d7abf2b57c96e891f5"></a>

### `RTS5912_GPIO103`

```c
#define RTS5912_GPIO103 &gpiog 7
```

<a id="a003e66685e2bb853e22026ee20c9f32e"></a>

### `RTS5912_GPIO104`

```c
#define RTS5912_GPIO104 &gpiog 8
```

<a id="a8129b0863a2d5bdcbe68be9d867ba6f9"></a>

### `RTS5912_GPIO105`

```c
#define RTS5912_GPIO105 &gpiog 9
```

<a id="a6f455cb1dea82764502381e47355ddc0"></a>

### `RTS5912_GPIO106`

```c
#define RTS5912_GPIO106 &gpiog 10
```

<a id="a0a7b9479655fd826fab1f3b14e5b0b77"></a>

### `RTS5912_GPIO107`

```c
#define RTS5912_GPIO107 &gpiog 11
```

<a id="a3b4910c5ff979f29d2565313862c4ea9"></a>

### `RTS5912_GPIO108`

```c
#define RTS5912_GPIO108 &gpiog 12
```

<a id="a9cd237a023d2c74c2d58c30a90771521"></a>

### `RTS5912_GPIO109`

```c
#define RTS5912_GPIO109 &gpiog 13
```

<a id="a1ed72627549ba6a83e2354845fa2d4a3"></a>

### `RTS5912_GPIO111`

```c
#define RTS5912_GPIO111 &gpiog 15
```

<a id="a24607480aae6f79e2ef88a231b15cead"></a>

### `RTS5912_GPIO112`

```c
#define RTS5912_GPIO112 &gpioh 0
```

<a id="aee14981a7bf40b01892b73422ecb1430"></a>

### `RTS5912_GPIO113`

```c
#define RTS5912_GPIO113 &gpioh 1
```

<a id="abda47f90d482d3cfe2055f4168096c25"></a>

### `RTS5912_GPIO114`

```c
#define RTS5912_GPIO114 &gpioh 2
```

<a id="a16a02bdb746fddfb6956cb9a286678d6"></a>

### `RTS5912_GPIO115`

```c
#define RTS5912_GPIO115 &gpioh 3
```

<a id="a9ee03b46798cab05c215e3536db77bfb"></a>

### `RTS5912_GPIO117`

```c
#define RTS5912_GPIO117 &gpioh 5
```

<a id="a2297d78143290ac827b4532bb71f94cc"></a>

### `RTS5912_GPIO118`

```c
#define RTS5912_GPIO118 &gpioh 6
```

<a id="ad81fc0b32d6eeca09e58c80aae92d5bc"></a>

### `RTS5912_GPIO119`

```c
#define RTS5912_GPIO119 &gpioh 7
```

<a id="afc2ee390daa1e132d0638e780637e224"></a>

### `RTS5912_GPIO120`

```c
#define RTS5912_GPIO120 &gpioh 8
```

<a id="aed0d9cc26a90e7e7c687186494836adf"></a>

### `RTS5912_GPIO121`

```c
#define RTS5912_GPIO121 &gpioh 9
```

<a id="aec88be11094c0589773fa285032c9a56"></a>

### `RTS5912_GPIO122`

```c
#define RTS5912_GPIO122 &gpioh 10
```

<a id="aabe0dc95aa117ee0c669827be4e97481"></a>

### `RTS5912_GPIO123`

```c
#define RTS5912_GPIO123 &gpioh 11
```

<a id="a8ae5b6fe831cab6aef485377453e8634"></a>

### `RTS5912_GPIO124`

```c
#define RTS5912_GPIO124 &gpioh 12
```

<a id="a2418255405a582a6d7974ffd995735fd"></a>

### `RTS5912_GPIO125`

```c
#define RTS5912_GPIO125 &gpioh 13
```

<a id="aad4ff9bb48086611f205c1b362b11881"></a>

### `RTS5912_GPIO126`

```c
#define RTS5912_GPIO126 &gpioh 14
```

<a id="a7394601627c978cdcbcc46234878cb6c"></a>

### `RTS5912_GPIO127`

```c
#define RTS5912_GPIO127 &gpioh 15
```

<a id="abeca8744b42ebe3f04594064f352187d"></a>

### `RTS5912_GPIO128`

```c
#define RTS5912_GPIO128 &gpioi 0
```

<a id="afc4124ad28042361d67ed609dfcf0da7"></a>

### `RTS5912_GPIO130`

```c
#define RTS5912_GPIO130 &gpioi 2
```

<a id="ada607c13918188d3f629363d143ea6cf"></a>

### `RTS5912_GPIO131`

```c
#define RTS5912_GPIO131 &gpioi 3
```

<a id="ae59327ac268671ea2e20014f17701529"></a>

### `RTS5912_GPIO_INDETEN`

```c
#define RTS5912_GPIO_INDETEN BIT(8)
```

启用输入检测（Input Detect）。

<a id="a471603d5ffb1be381681a56d19b54757"></a>

### `RTS5912_GPIO_INTR_MASK`

```c
#define RTS5912_GPIO_INTR_MASK (1U << 21 | 1U << 22 | 1U << 24 | 1U << 25 | 1U << 26)
```

中断掩码（Interrupt Mask），因为 RTS5912 不支持 `GPIO_INT_LEVELS_LOGICAL`。

<a id="a93faaacf50a46b2209231e7eae2da8b4"></a>

### `RTS5912_GPIO_MFCTRL_0`

```c
#define RTS5912_GPIO_MFCTRL_0 (0U << RTS5912_GPIO_MFCTRL_POS)
```

`0x00`：功能 0；`0x01`：功能 1；`0x02`：功能 2；`0x03`：功能 3（Function 0–3）。

<a id="adf7208d3ffb32ee5f1d65deff41aaa74"></a>

### `RTS5912_GPIO_MFCTRL_1`

```c
#define RTS5912_GPIO_MFCTRL_1 (1U << RTS5912_GPIO_MFCTRL_POS)
```

<a id="ae492ac80b7741521601d6885d2f1b530"></a>

### `RTS5912_GPIO_MFCTRL_2`

```c
#define RTS5912_GPIO_MFCTRL_2 (2U << RTS5912_GPIO_MFCTRL_POS)
```

<a id="abf987c5c5f861c3d2ff57c664264acd0"></a>

### `RTS5912_GPIO_MFCTRL_3`

```c
#define RTS5912_GPIO_MFCTRL_3 (3U << RTS5912_GPIO_MFCTRL_POS)
```

<a id="a661de5a3eb9f6b97f44735718c29dc43"></a>

### `RTS5912_GPIO_MFCTRL_MASK`

```c
#define RTS5912_GPIO_MFCTRL_MASK GENMASK(15, 14)
```

<a id="acea96124332b298d7f413105ed2c430f"></a>

### `RTS5912_GPIO_MFCTRL_POS`

```c
#define RTS5912_GPIO_MFCTRL_POS 14
```

多功能（Multi Function）。

<a id="a9f3289747c68c46fa5d8f92ebe0e2283"></a>

### `RTS5912_GPIO_OUTDRV`

```c
#define RTS5912_GPIO_OUTDRV BIT(9)
```

设置引脚驱动电流（Pin Driving Current）。

<a id="ae65d41879bcb126213ac007808086cee"></a>

### `RTS5912_GPIO_SCHEN`

```c
#define RTS5912_GPIO_SCHEN BIT(11)
```

启用施密特触发器（Schmitt Trigger）。

<a id="aa5af355318f8b6a034b85ed418de6cdd"></a>

### `RTS5912_GPIO_SLEWRATE`

```c
#define RTS5912_GPIO_SLEWRATE BIT(10)
```

设置 GPIO 转换速率（Slew Rate）。

<a id="a83d8d0f0a827e770de9fe360fe566573"></a>

### `RTS5912_GPIO_VOLTAGE_1V8`

```c
#define RTS5912_GPIO_VOLTAGE_1V8 (1U << RTS5912_GPIO_VOLTAGE_POS)
```

将引脚电压电平（Pin Voltage Level）设置为 1.8 V。

<a id="a24268d0667f7a2266e519c03e6a04395"></a>

### `RTS5912_GPIO_VOLTAGE_3V3`

```c
#define RTS5912_GPIO_VOLTAGE_3V3 (2U << RTS5912_GPIO_VOLTAGE_POS)
```

将引脚电压电平（Pin Voltage Level）设置为 3.3 V。

<a id="a0ca327e5b979185b539f187eabcbc0be"></a>

### `RTS5912_GPIO_VOLTAGE_5V0`

```c
#define RTS5912_GPIO_VOLTAGE_5V0 (3U << RTS5912_GPIO_VOLTAGE_POS)
```

将引脚电压电平（Pin Voltage Level）设置为 5.0 V。

<a id="a91e7d587b96806b3f8403d3532d5a888"></a>

### `RTS5912_GPIO_VOLTAGE_DEFAULT`

```c
#define RTS5912_GPIO_VOLTAGE_DEFAULT (0U << RTS5912_GPIO_VOLTAGE_POS)
```

将引脚设置为默认电压电平（Default Voltage Level）。

<a id="a9ab90e903840aec5172596492f12e6b5"></a>

### `RTS5912_GPIO_VOLTAGE_MASK`

```c
#define RTS5912_GPIO_VOLTAGE_MASK GENMASK(13, 12)
```

<a id="a0381dff71143b0fadceaaade950340a3"></a>

### `RTS5912_GPIO_VOLTAGE_POS`

```c
#define RTS5912_GPIO_VOLTAGE_POS 12
```


## 29.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P159_realtek-gpio.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P028_zephyr__drivers__pwm__pwm_utils.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__dt-bindings__power__rpi_bcm283x_power.h_文件参考.md)
