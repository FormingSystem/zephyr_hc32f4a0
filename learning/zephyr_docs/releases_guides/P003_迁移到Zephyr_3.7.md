---
id: learning.zephyr-docs.releases-guides.page-3
title: 迁移到Zephyr 3.7
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/migration-guide-3.7.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="migration-guide-to-zephyr-v3-7-0"></a>

<a id="migration-3-7"></a>

# 第3章\_迁移到Zephyr v3.7.0的指南

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/migration-guide-3.7.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

本文描述将应用从Zephyr v3.6.0迁移到v3.7.0所需的更改。

其他与应用迁移没有直接关系的变化，见发行说明。（[发行说明（Release Notes）](https://docs.zephyrproject.org/latest/releases/release-notes-3.7.html#zephyr-3-7)）

<a id="contents"></a>


- <a id="id1"></a>

  [构建系统（Build System）](#build-system)
- <a id="id2"></a>

  [内核（Kernel）](#kernel)
- <a id="id3"></a>

  [开发板（Boards）](#boards)
- <a id="id4"></a>

  [模块（Modules）](#modules)


  - <a id="id5"></a>

    [Mbed TLS密码与TLS库](#mbed-tls)
  - <a id="id6"></a>

    [可信固件M（Trusted Firmware-M）](#trusted-firmware-m)
  - <a id="id7"></a>

    [轻量图形库（LVGL）](#lvgl)
- <a id="id8"></a>

  [设备驱动与设备树（Device Drivers and Devicetree）](#device-drivers-and-devicetree)


  - <a id="id9"></a>

    [充电器（Charger）](#charger)
  - <a id="id10"></a>

    [控制器局域网（Controller Area Network，CAN）](#controller-area-network-can)
  - <a id="id11"></a>

    [密码功能（Crypto）](#crypto)
  - <a id="id12"></a>

    [显示（Display）](#display)
  - <a id="id13"></a>

    [增强型串行外设接口（Enhanced SPI，eSPI）](#enhanced-serial-peripheral-interface-espi)
  - <a id="id14"></a>

    [全球导航卫星系统（GNSS）](#gnss)
  - <a id="id15"></a>

    [输入（Input）](#input)
  - <a id="id16"></a>

    [中断控制器（Interrupt Controller）](#interrupt-controller)
  - <a id="id17"></a>

    [LED灯带（LED Strip）](#led-strip)
  - <a id="id18"></a>

    [管理数据输入输出（MDIO）](#mdio)
  - <a id="id19"></a>

    [传感器（Sensors）](#sensors)
  - <a id="id20"></a>

    [串行接口（Serial）](#serial)
  - <a id="id21"></a>

    [稳压器（Regulator）](#regulator)
  - <a id="id22"></a>

    [单线总线（W1）](#w1)
  - <a id="id23"></a>

    [看门狗（Watchdog）](#watchdog)
- <a id="id24"></a>

  [蓝牙（Bluetooth）](#bluetooth)


  - <a id="id25"></a>

    [蓝牙主机控制器接口（Bluetooth HCI）](#bluetooth-hci)
  - <a id="id26"></a>

    [蓝牙网状网络（Bluetooth Mesh）](#bluetooth-mesh)
  - <a id="id27"></a>

    [蓝牙音频（Bluetooth Audio）](#bluetooth-audio)
  - <a id="id28"></a>

    [经典蓝牙（Bluetooth Classic）](#bluetooth-classic)
  - <a id="id29"></a>

    [蓝牙主机（Bluetooth Host）](#bluetooth-host)
  - <a id="id30"></a>

    [蓝牙密码功能（Bluetooth Crypto）](#bluetooth-crypto)
- <a id="id31"></a>

  [网络（Networking）](#networking)
- <a id="id32"></a>

  [其他子系统（Other Subsystems）](#other-subsystems)


  - <a id="id33"></a>

    [Flash映射（Flash Map）](#flash-map)
  - <a id="id34"></a>

    [设备更新服务（hawkBit）](#hawkbit)
  - <a id="id35"></a>

    [微控制器管理（MCUmgr）](#mcumgr)
  - <a id="id36"></a>

    [调制解调器（Modem）](#modem)
  - <a id="id37"></a>

    [POSIX应用编程接口（POSIX API）](#posix-api)
  - <a id="id38"></a>

    [状态机框架（State Machine Framework）](#state-machine-framework)
  - <a id="id39"></a>

    [固件更新服务（UpdateHub）](#updatehub)
- <a id="id40"></a>

  [架构（Architectures）](#architectures)

<a id="build-system"></a>

## [构建系统（Build System）](#id1)


- 全面改造SoC及开发板的定义方式。所有树外SoC及开发板都必须移植到新模型，详情见“过渡到当前硬件模型（Transition to the Current Hardware Model）”。（[GitHub #69607](https://github.com/zephyrproject-rtos/zephyr/issues/69607)）（[迁移到当前硬件模型](https://docs.zephyrproject.org/latest/hardware/porting/board_porting.html#hw-model-v2)）
- 以下构建时生成的头文件：

  <table>
  <tr>
  <th>受影响头文件（Affected Header Files）</th>
  </tr>
  <tr>
  <td><code>app_version.h</code></td>
  </tr>
  <tr>
  <td><code>autoconf.h</code></td>
  </tr>
  <tr>
  <td><code>cmake_intdef.h</code></td>
  </tr>
  <tr>
  <td><code>core-isa-dM.h</code></td>
  </tr>
  <tr>
  <td><code>devicetree_generated.h</code></td>
  </tr>
  <tr>
  <td><code>driver-validation.h</code></td>
  </tr>
  <tr>
  <td><code>kobj-types-enum.h</code></td>
  </tr>
  <tr>
  <td><code>linker-kobject-prebuilt-data.h</code></td>
  </tr>
  <tr>
  <td><code>linker-kobject-prebuilt-priv-stacks.h</code></td>
  </tr>
  <tr>
  <td><code>linker-kobject-prebuilt-rodata.h</code></td>
  </tr>
  <tr>
  <td><code>mcuboot_version.h</code></td>
  </tr>
  <tr>
  <td><code>offsets.h</code></td>
  </tr>
  <tr>
  <td><code>otype-to-size.h</code></td>
  </tr>
  <tr>
  <td><code>otype-to-str.h</code></td>
  </tr>
  <tr>
  <td><code>strerror_table.h</code></td>
  </tr>
  <tr>
  <td><code>strsignal_table.h</code></td>
  </tr>
  <tr>
  <td><code>syscall_list.h</code></td>
  </tr>
  <tr>
  <td><code>version.h</code></td>
  </tr>
  <tr>
  <td><code>zsr.h</code></td>
  </tr>
  </table>

  以及系统调用头文件及源码，现在均放入zephyr/目录形成命名空间。大部分修改可自动完成，脚本见[GitHub #63973](https://github.com/zephyrproject-rtos/zephyr/issues/63973)。目前兼容性Kconfig选项[CONFIG_LEGACY_GENERATED_INCLUDE_PATH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LEGACY_GENERATED_INCLUDE_PATH)默认启用，因此下游应用仍可编译，但CMake配置时会给出警告。该选项将被弃用并最终移除，建议开发者尽快更新这些头文件的包含路径。

<a id="kernel"></a>

## [内核（Kernel）](#id2)


- 所有架构现在都必须定义新的struct arch_esf，用于描述栈帧成员；它替代命名结构体struct z_arch_esf_t。（[GitHub #73593](https://github.com/zephyrproject-rtos/zephyr/issues/73593)）
- 命名结构体struct z_arch_esf_t现已弃用，请改用struct arch_esf。（[GitHub #73593](https://github.com/zephyrproject-rtos/zephyr/issues/73593)）
- 头文件[include/zephyr/arch/arch_interface.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/arch/arch_interface.h)已从include/zephyr/sys/移到include/zephyr/arch/，树外源码须更新包含路径。（[GitHub #64987](https://github.com/zephyrproject-rtos/zephyr/issues/64987)）

<a id="boards"></a>

## [开发板（Boards）](#id3)


- 调整SparkFun Pro Micro RP2040的pro_micro连接器gpio-map中D1及D0顺序，以匹配原始Pro Micro定义；树外扩展板须相应更新。（[GitHub #69994](https://github.com/zephyrproject-rtos/zephyr/issues/69994)）
- ITE：重命名所有SoC变体Kconfig选项，例如CONFIG_SOC_IT82202_AX改为CONFIG_SOC_IT82202AX。新符号为SOC_IT81202BX、SOC_IT81202CX、SOC_IT81302BX、SOC_IT81302CX、SOC_IT82002AW、SOC_IT82202AX及SOC_IT82302AX；SOC_SERIES_ITE_IT8XXX2也改为SOC_SERIES_IT8XXX2。（[GitHub #71680](https://github.com/zephyrproject-rtos/zephyr/issues/71680)）
- 对native_sim/posix，设置[CONFIG_I2C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)时不再默认启用[CONFIG_EMUL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)，需要时应在项目配置文件中明确启用。（[GitHub #73067](https://github.com/zephyrproject-rtos/zephyr/issues/73067)）
- LiteX：VexRiscV中断控制器节点的compatible从vexriscv-intc0改为[litex,vexriscv-intc0](../soc_interrupt_binding_reference/P009_litex_vexriscv-intc0.md#std-dtcompatible-litex-vexriscv-intc0)。（[GitHub #73211](https://github.com/zephyrproject-rtos/zephyr/issues/73211)）
- lairdconnect开发板现在归入ezurio，因为Laird Connectivity已更名为[Ezurio](https://www.ezurio.com/laird-connectivity)。

<a id="modules"></a>

## [模块（Modules）](#id4)

<a id="mbed-tls"></a>

### [Mbed TLS密码与TLS库](#id5)


- TLS 1.2、RSA、AES、DES，以及除SHA-256之外的所有哈希算法，即SHA-224、SHA-384、SHA-512、MD5及SHA-1，均不再默认启用。使用时须明确启用相应Kconfig选项。（[GitHub #72078](https://github.com/zephyrproject-rtos/zephyr/issues/72078)）
- 原名CONFIG_MBEDTLS_MAC_*_ENABLED的Kconfig选项已重命名，去掉名称中的_MAC及_ENABLED。（[GitHub #73267](https://github.com/zephyrproject-rtos/zephyr/issues/73267)）
- 修复[CONFIG_MBEDTLS_HASH_ALL_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_HASH_ALL_ENABLED)，使其确实启用所有可用哈希算法；此前仅启用SHA-2系列。（[GitHub #73267](https://github.com/zephyrproject-rtos/zephyr/issues/73267)）
- 移除CONFIG_MBEDTLS_HASH_SHA*_ENABLED选项，它们与现在名为CONFIG_MBEDTLS_SHA*的其他选项重复。（[GitHub #73267](https://github.com/zephyrproject-rtos/zephyr/issues/73267)）
- 移除CONFIG_MBEDTLS_MAC_ALL_ENABLED，等效配置为同时使用[CONFIG_MBEDTLS_HASH_ALL_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_HASH_ALL_ENABLED)及CONFIG_MBEDTLS_CMAC。（[GitHub #73267](https://github.com/zephyrproject-rtos/zephyr/issues/73267)）
- 移除CONFIG_MBEDTLS_MAC_MD4_ENABLED、CONFIG_MBEDTLS_CIPHER_ARC4_ENABLED及CONFIG_MBEDTLS_CIPHER_BLOWFISH_ENABLED，因为Mbed TLS已不再支持对应算法。（[GitHub #73222](https://github.com/zephyrproject-rtos/zephyr/issues/73222)）
- 系统中存在任意PSA密码服务提供者，即设置CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT时，必须通过相应CONFIG_PSA_WANT_*明确启用所需PSA密码功能。（[GitHub #72243](https://github.com/zephyrproject-rtos/zephyr/issues/72243)）
- 只要系统中存在任意PSA密码服务提供者，即设置CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT，TLS／X509／PK／MD模块就会改用PSA密码API，而不再使用旧API。（[GitHub #72243](https://github.com/zephyrproject-rtos/zephyr/issues/72243)）

<a id="trusted-firmware-m"></a>

### [可信固件M（Trusted Firmware-M）](#id6)


- MCUboot默认签名类型由RSA-3072改为EC-P256，影响在TF-M中启用MCUboot，即[CONFIG_TFM_BL2](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_BL2)的构建。若要继续使用RSA-3072，须将[CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE)设为"RSA-3072"；否则应确保自己的签名密钥与实际签名类型匹配。

<a id="lvgl"></a>

### [轻量图形库（LVGL）](#id7)


- 移除CONFIG_LV_Z_POINTER_KSCAN。须将基于kscan的驱动转换到输入子系统，并在设备树中改用[zephyr,lvgl-pointer-input](../input_touch_lvgl_gesture_binding_reference/P020_zephyr_lvgl-pointer-input.md#std-dtcompatible-zephyr-lvgl-pointer-input)。（[GitHub #73800](https://github.com/zephyrproject-rtos/zephyr/issues/73800)）

<a id="device-drivers-and-devicetree"></a>

## [设备驱动与设备树（Device Drivers and Devicetree）](#id8)


- nxp,kinetis-pit驱动的compatible改为[nxp,pit](../nxp_nuvoton_counter_binding_reference/P017_nxp_pit.md#std-dtcompatible-nxp-pit)，并增加多通道支持。配置各通道时，必须添加compatible为[nxp,pit-channel](../nxp_nuvoton_counter_binding_reference/P016_nxp_pit-channel.md#std-dtcompatible-nxp-pit-channel)的子节点，并按下面方式配置。随着PIT绑定重命名，CONFIG_COUNTER_MCUX_PIT也改为[CONFIG_COUNTER_NXP_PIT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_NXP_PIT)。（[GitHub #66336](https://github.com/zephyrproject-rtos/zephyr/issues/66336)）示例：

  ```text
  / {
      pit0: pit@40037000 {
          /* Other Pit DT Attributes */
          compatible = "nxp,pit";
          status = "disabled";
          num-channels = <1>;
          #address-cells = <1>;
          #size-cells = <0>;

          pit0_channel0: pit0_channel@0 {
              compatible = "nxp,pit-channel";
              reg = <0>;
              status = "disabled";
          };
  };
  ```
- nxp,kinetis-ethernet已弃用，改用[nxp,enet](../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet)。树内所有SoC均已转换，因此使用NXP ENET外设的开发板都须调整设备树以匹配新绑定，并使用相应的新版本驱动。也可删除以太网节点，按旧绑定重新定义，继续使用已弃用的旧驱动。新绑定主要优势是通过MDIO API抽象任意PHY。（[GitHub #70400](https://github.com/zephyrproject-rtos/zephyr/issues/70400)）基本板级ENET设备树定义示例：

  ```text
  &enet_mac {
      status = "okay";
      pinctrl-0 = <&pinmux_enet>;
      pinctrl-names = "default";
      phy-handle = <&phy>;
      zephyr,random-mac-address;
      phy-connection-type = "rmii";
  };

  &enet_mdio {
      status = "okay";
      pinctrl-0 = <&pinmux_enet_mdio>;
      pinctrl-names = "default";
      phy: phy@3 {
          compatible = "ethernet-phy";
          reg = <3>;
          status = "okay";
      };
  };
  ```
- compatible字符串nxp,kinetis-lptmr改为[nxp,lptmr](../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr)。旧字符串短期内仍可使用，但今后会移除，应尽快替换。
- 部分驱动API结构体已重命名，以具备要求的_driver_api后缀。（[GitHub #72182](https://github.com/zephyrproject-rtos/zephyr/issues/72182)）重命名类型如下：


  - emul_sensor_backend_api改为emul_sensor_driver_api
  - emul_bbram_backend_api改为emul_bbram_driver_api
  - usbc_ppc_drv改为[usbc_ppc_driver_api](https://docs.zephyrproject.org/latest/doxygen/html/structusbc__ppc__driver__api.html)
- [maxim,max31790](../hardware/P710_MAX31790多功能设备绑定.md#dtbinding-maxim-max31790)驱动拆分为多功能设备MFD及实际PWM驱动。（[GitHub #68433](https://github.com/zephyrproject-rtos/zephyr/issues/68433)）以前设备实例可能定义为：

  ```text
  max31790_max31790: max31790@20 {
      compatible = "maxim,max31790";
      status = "okay";
      reg = <0x20>;
      pwm-controller;
      #pwm-cells = <2>;
  };
  ```

  现在可转换为：

  ```text
  max31790_max31790: max31790@20 {
      compatible = "maxim,max31790";
      status = "okay";
      reg = <0x20>;

      max31790_max31790_pwm: max31790_max31790_pwm {
          compatible = "maxim,max31790-pwm";
          status = "okay";
          pwm-controller;
          #pwm-cells = <2>;
      };
  };
  ```
- [invensense,icm42688](../sensor_espressif_honeywell_invensense_binding_reference/P028_invensense_icm42688.md#std-dtcompatible-invensense-icm42688)驱动现在正确支持设备树配置。（[GitHub #74267](https://github.com/zephyrproject-rtos/zephyr/issues/74267)）以前设备树可能尝试通过绑定设置加速度计／陀螺仪采样率及量程，但实际上无效；现在应结合提供的宏定义及头文件，使用接收这些值的新绑定。

  例如：

  ```text
  #include <zephyr/dt-bindings/sensor/icm42688.h>

  icm42688: icm42688@0 {
      accel-pwr-mode = <ICM42688_ACCEL_LN>;
      accel-fs = <ICM42688_ACCEL_FS_16G>;
      accel-odr = <ICM42688_ACCEL_ODR_2000>;
      gyro-pwr-mode= <ICM42688_GYRO_LN>;
      gyro-fs = <ICM42688_GYRO_FS_2000>;
      gyro-odr = <ICM42688_GYRO_ODR_2000>;
  };
  ```
- [st,lis2mdl](../compatible_binding_reference/P085_st_lis2mdl.md#std-dtcompatible-st-lis2mdl)的spi-full-duplex属性改为duplex = SPI_FULL_DUPLEX；全双工现在是默认模式。
- 移除[nxp,lpc-lpadc](../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc)驱动的nxp,reference-supply设备树属性，用户应从设备树中删除。新增phandle-array类型属性nxp,references，可用来指定LPADC所用参考电压源及其电压值。（[GitHub #75005](https://github.com/zephyrproject-rtos/zephyr/issues/75005)）

> - [microchip,ksz8081](../ethernet_phy_renesas_rockchip_binding_reference/P001_microchip_ksz8081.md#std-dtcompatible-microchip-ksz8081) PHY绑定的mc,interface-type、mc,reset-gpio及mc,interrupt-gpio属性，分别改为microchip,interface-type、reset-gpios及int-gpios。（[GitHub #73725](https://github.com/zephyrproject-rtos/zephyr/issues/73725)）

<a id="charger"></a>

### [充电器（Charger）](#id9)


- 移除charger_max20335驱动的constant-charge-current-max-microamp属性，因为它不符合芯片实际功能。（[GitHub #69910](https://github.com/zephyrproject-rtos/zephyr/issues/69910)）
- 为maxim,max20335-charger绑定的constant-charge-voltage-max-microvolt属性添加enum键，以便构建时检测无效设备树值。（[GitHub #69910](https://github.com/zephyrproject-rtos/zephyr/issues/69910)）

<a id="controller-area-network-can"></a>

### [控制器局域网（Controller Area Network，CAN）](#id10)


- 移除以下已弃用的CAN控制器设备树属性。树外开发板可改用bitrate、sample-point、bitrate-data及sample-point-data，或依赖[CONFIG_CAN_DEFAULT_BITRATE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_DEFAULT_BITRATE)及[CONFIG_CAN_DEFAULT_BITRATE_DATA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_DEFAULT_BITRATE_DATA)，指定初始CAN比特率：


  - `sjw`
  - `prop-seg`
  - `phase-seg1`
  - `phase-seg2`
  - `sjw-data`
  - `prop-seg-data`
  - `phase-seg1-data`
  - `phase-seg2-data`

  CAN控制器设备树属性bus-speed及bus-speed-data已弃用。

  参见[GitHub #68714](https://github.com/zephyrproject-rtos/zephyr/issues/68714)。
- 重新设计手动总线关闭恢复（Bus-off Recovery）支持。（[GitHub #69460](https://github.com/zephyrproject-rtos/zephyr/issues/69460)）


  - 无论Kconfig如何设置，驱动初始化时始终启用自动总线恢复。CAN控制器初始化时处于停止状态，因此此时不会启动意外的bus-off恢复。
  - CONFIG_CAN_AUTO_BUS_OFF_RECOVERY重命名并反转语义，改为默认禁用的[CONFIG_CAN_MANUAL_RECOVERY_MODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MANUAL_RECOVERY_MODE)。它启用[can_recover()](../hardware/P362_CAN控制器接口.md#gac474e56a50685736a1c25dca277aab5e) API及新的手动恢复模式，见下一项。
  - 新增CAN控制器运行模式[CAN_MODE_MANUAL_RECOVERY](../hardware/P362_CAN控制器接口.md#ga3d8675253125b2af2bd22f0b2cc60cdd)，仅在启用[CONFIG_CAN_MANUAL_RECOVERY_MODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MANUAL_RECOVERY_MODE)时支持。将其作为模式后，应用可通过[can_get_capabilities()](../hardware/P362_CAN控制器接口.md#ga4afd7776c5039dec8acb089499dc1168)查询控制器是否支持手动恢复，再决定初始化失败还是依赖自动bus-off恢复。这样，不支持手动恢复的驱动可在应用启动调用[can_set_mode()](../hardware/P362_CAN控制器接口.md#gae04c3c884b3ed26dfea4745b7dff2c5f)时尽早失败，而不必等到稍后调用[can_recover()](../hardware/P362_CAN控制器接口.md#gac474e56a50685736a1c25dca277aab5e)时才失败。

<a id="crypto"></a>

### [密码功能（Crypto）](#id11)


- NXP lpc55s36上的CSS驱动已弃用。（[GitHub #71173](https://github.com/zephyrproject-rtos/zephyr/issues/71173)）

<a id="display"></a>

### [显示（Display）](#id12)


- 基于GC9X01的显示屏改用MIPI DBI驱动类，必须放在负责与显示屏通信的MIPI DBI驱动包装设备内声明。（[GitHub #73686](https://github.com/zephyrproject-rtos/zephyr/issues/73686)）示例见下文：

  ```text
  /* Legacy GC9X01 display definition */
  &spi0 {
      gc9a01: gc9a01@0 {
          status = "okay";
          compatible = "galaxycore,gc9x01x";
          reg = <0>;
          spi-max-frequency = <100000000>;
          cmd-data-gpios = <&gpio0 8 GPIO_ACTIVE_HIGH>;
          reset-gpios = <&gpio0 14 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      dc-gpios = <&gpio0 8 GPIO_ACTIVE_HIGH>;
      reset-gpios = <&gpio0 14 GPIO_ACTIVE_LOW>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;

      gc9a01: gc9a01@0 {
          status = "okay";
          compatible = "galaxycore,gc9x01x";
          reg = <0>;
          mipi-max-frequency = <100000000>;
          ...
      };
  };
  ```
- 基于ST7735R的显示屏改用MIPI DBI驱动类，必须放在负责通信的MIPI DBI驱动包装设备内声明。此次更新改变了cmd-data-gpios引脚极性，以匹配新名称dc-gpios。示例见下文：

  ```text
  /* Legacy ST7735R display definition */
  &spi0 {
      st7735r: st7735r@0 {
          compatible = "sitronix,st7735r";
          reg = <0>;
          spi-max-frequency = <32000000>;
          reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
          cmd-data-gpios = <&gpio0 12 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
      dc-gpios = <&gpio0 12 GPIO_ACTIVE_HIGH>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;

      st7735r: st7735r@0 {
          compatible = "sitronix,st7735r";
          reg = <0>;
          mipi-max-frequency = <32000000>;
          mipi-mode = <MIPI_DBI_MODE_SPI_4WIRE>;
          ...
      };
  };
  ```
- 基于UC81XX的显示屏改用MIPI DBI驱动类，必须放在负责通信的MIPI DBI驱动包装设备内声明。（[GitHub #73812](https://github.com/zephyrproject-rtos/zephyr/issues/73812)）此次更新改变了dc-gpios引脚极性，示例见下文：

  ```text
  /* Legacy UC81XX display definition */
  &spi0 {
      uc8179: uc8179@0 {
          compatible = "ultrachip,uc8179";
          reg = <0>;
          spi-max-frequency = <4000000>;
          reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
          dc-gpios = <&gpio0 12 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
      dc-gpios = <&gpio0 12 GPIO_ACTIVE_HIGH>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;
      uc8179: uc8179@0 {
          compatible = "ultrachip,uc8179";
          reg = <0>;
          mipi-max-frequency = <4000000>;
          ...
      };
  };
  ```
- 基于ST7789V的显示屏改用MIPI DBI驱动类，必须放在负责通信的MIPI DBI驱动包装设备内声明。（[GitHub #73750](https://github.com/zephyrproject-rtos/zephyr/issues/73750)）此次更新改变了cmd-data-gpios引脚极性，以匹配新名称dc-gpios。示例见下文：

  ```text
  /* Legacy ST7789V display definition */
  &spi0 {
      st7789: st7789@0 {
          compatible = "sitronix,st7789v";
          reg = <0>;
          spi-max-frequency = <32000000>;
          reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
          cmd-data-gpios = <&gpio0 12 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
      dc-gpios = <&gpio0 12 GPIO_ACTIVE_HIGH>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;

      st7789: st7789@0 {
          compatible = "sitronix,st7789v";
          reg = <0>;
          mipi-max-frequency = <32000000>;
          mipi-mode = <MIPI_DBI_MODE_SPI_4WIRE>;
          ...
      };
  };
  ```
- 基于SSD16XX的显示屏改用MIPI DBI驱动类。（[GitHub #73946](https://github.com/zephyrproject-rtos/zephyr/issues/73946)）必须放在负责通信的MIPI DBI驱动包装设备内声明；此次更新改变了dc-gpios引脚极性。示例见下文：

  ```text
  /* Legacy SSD16XX display definition */
  &spi0 {
      ssd1680: ssd1680@0 {
          compatible = "solomon,ssd1680";
          reg = <0>;
          spi-max-frequency = <4000000>;
          reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
          dc-gpios = <&gpio0 12 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
      dc-gpios = <&gpio0 12 GPIO_ACTIVE_HIGH>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;

      ssd1680: ssd1680@0 {
          compatible = "solomon,ssd1680";
          reg = <0>;
          mipi-max-frequency = <4000000>;
          ...
      };
  };
  ```
- SSD16XX显示驱动已支持显示旋转，因此移除orientation-flipped属性。用户应从设备树删除该属性，并在运行时通过[display_set_orientation()](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4e0a4dc2e434144874af014b8e7c4394)设置方向。（[GitHub #73360](https://github.com/zephyrproject-rtos/zephyr/issues/73360)）

<a id="enhanced-serial-peripheral-interface-espi"></a>

### [增强型串行外设接口（Enhanced SPI，eSPI）](#id13)


- 为采用eSPI 1.5规范新术语，ESPI_SLAVE_TO_MASTER及ESPI_MASTER_TO_SLAVE分别改名为ESPI_TARGET_TO_CONTROLLER及ESPI_CONTROLLER_TO_TARGET；枚举ESPI_VWIRE_SIGNAL_SLV_BOOT_STS、ESPI_VWIRE_SIGNAL_SLV_BOOT_DONE及所有ESPI_VWIRE_SIGNAL_SLV_GPIO_<NUMBER>，分别改为ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS、ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE及ESPI_VWIRE_SIGNAL_TARGET_GPIO_<NUMBER>。（[GitHub #68492](https://github.com/zephyrproject-rtos/zephyr/issues/68492)）CONFIG_ESPI_SLAVE改为[CONFIG_ESPI_TARGET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPI_TARGET)，CONFIG_ESPI_SAF改为[CONFIG_ESPI_TAF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPI_TAF)。（[GitHub #73887](https://github.com/zephyrproject-rtos/zephyr/issues/73887)）

<a id="gnss"></a>

### [全球导航卫星系统（GNSS）](#id14)


- gnss-nmea-generic驱动新增基本电源管理支持。设置CONFIG_PM_DEVICE=y时，驱动以挂起状态初始化；应用必须调用[pm_device_action_run()](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#ga3840d6e7832a00b93763247a5951bfde)并传入PM_DEVICE_ACTION_RESUME，才能启动驱动。（[GitHub #71774](https://github.com/zephyrproject-rtos/zephyr/issues/71774)）

<a id="input"></a>

### [输入（Input）](#id15)


- analog-axis死区校准值改为相对原始ADC值，与min及max一致。相关数据结构和属性由out-deadzone改名为in-deadzone，迁移到新定义时应相应缩放该值。（[GitHub #70377](https://github.com/zephyrproject-rtos/zephyr/issues/70377)）
- holtek,ht16k33-keyscan驱动已转换为使用输入子系统，回调须迁移到输入API；可用zephyr,kscan-input保持向后兼容。（[GitHub #69875](https://github.com/zephyrproject-rtos/zephyr/issues/69875)）（[输入（Input）](https://docs.zephyrproject.org/latest/services/input/index.html#input)）

<a id="interrupt-controller"></a>

### [中断控制器（Interrupt Controller）](#id16)


- 多级中断控制器查找表的静态自动生成方式已弃用，仅在启用新兼容性选项CONFIG_LEGACY_MULTI_LEVEL_TABLE_GENERATION时编译，该选项会在后续版本移除。

  多级中断控制器驱动应改用新宏IRQ_PARENT_ENTRY_DEFINE，将自身注册到新的多级中断架构。为简化使用，INTC_INST_ISR_TBL_OFFSET可推导给定驱动实例的软件ISR表偏移；伪中断控制器子节点应使用INTC_CHILD_ISR_TBL_OFFSET。新增DT_INTC_GET_AGGREGATOR_LEVEL及DT_INST_INTC_GET_AGGREGATOR_LEVEL设备树宏，让驱动实例向IRQ_PARENT_ENTRY_DEFINE传入其聚合器层级。

<a id="led-strip"></a>

### [LED灯带（LED Strip）](#id17)


- [worldsemi,ws2812-gpio](../led_strip_binding_reference/P008_worldsemi_ws2812-gpio.md#std-dtcompatible-worldsemi-ws2812-gpio)绑定中的in-gpios属性重命名为gpios。（[GitHub #68514](https://github.com/zephyrproject-rtos/zephyr/issues/68514)）
- 所有LED灯带绑定新增chain-length及color-mapping属性，二者现在均为必需。
- 新增必需的length函数，返回LED灯带设备长度，即像素数量。
- update_channels函数改为可选，并移除未实现的函数。
- 移除CONFIG_WS2812_STRIP_DRIVER。以前使用[CONFIG_WS2812_STRIP_SPI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WS2812_STRIP_SPI)、[CONFIG_WS2812_STRIP_I2S](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WS2812_STRIP_I2S)、[CONFIG_WS2812_STRIP_GPIO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WS2812_STRIP_GPIO)或[CONFIG_WS2812_STRIP_RPI_PICO_PIO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WS2812_STRIP_RPI_PICO_PIO)时，须通过CONFIG_WS2812_STRIP_DRIVER选择其中一个；现在不再需要，请直接设置相应选项。

<a id="mdio"></a>

### [管理数据输入输出（MDIO）](#id18)


- [CONFIG_MDIO_NXP_ENET_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDIO_NXP_ENET_TIMEOUT)的单位由毫秒改为微秒。（[GitHub #75625](https://github.com/zephyrproject-rtos/zephyr/issues/75625)）

<a id="sensors"></a>

### [传感器（Sensors）](#id19)


- 移除[sensirion,shtcx](../sensor_realtek_rohm_sensirion_binding_reference/P026_sensirion_shtcx.md#std-dtcompatible-sensirion-shtcx)传感器驱动的chip设备树属性，改用相应compatible选择芯片变体。（[GitHub #74033](https://github.com/zephyrproject-rtos/zephyr/issues/74033)）新的shtc3配置示例见下文：

  ```text
  &i2c0 {
      status = "okay";

      shtc3: shtc3@70 {
          compatible = "sensirion,shtc3", "sensirion,shtcx";
          reg = <0x70>;
          measure-mode = "normal";
          clock-stretching;
      };
  };
  ```

<a id="serial"></a>

### [串行接口（Serial）](#id20)


- 移除树莓派UART驱动uart_rpi_pico，改用uart_pl011，即[arm,pl011](../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011)。（[GitHub #71074](https://github.com/zephyrproject-rtos/zephyr/issues/71074)）

<a id="regulator"></a>

### [稳压器（Regulator）](#id21)


- [nxp,vref](../hardware/P652_NXP参考电压绑定.md#dtbinding-nxp-vref)驱动不再支持接地选择功能，因为用户不应修改该设置。已移除nxp,ground-select设备树属性，若设备树中存在该属性，应删除。（[GitHub #70642](https://github.com/zephyrproject-rtos/zephyr/issues/70642)）

<a id="w1"></a>

### [单线总线（W1）](#id22)


- [zephyr,w1-gpio](../mux_w1_binding_reference/P011_zephyr_w1-gpio.md#std-dtcompatible-zephyr-w1-gpio)单总线主驱动不再默认启用GPIO内部上拉，改为根据设备树中该引脚的配置标志决定。（[GitHub #71789](https://github.com/zephyrproject-rtos/zephyr/issues/71789)）

<a id="watchdog"></a>

### [看门狗（Watchdog）](#id23)


- nuvoton,npcx-watchdog驱动修改以扩展最大超时时间。不同预分频设置会改变单次看门狗计数的时间，因此移除不再适合设置提前告警时间的CONFIG_WDT_NPCX_DELAY_CYCLES，新增[CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS)，以毫秒设置提前告警时间。

<a id="bluetooth"></a>

## [蓝牙（Bluetooth）](#id24)

<a id="bluetooth-hci"></a>

### [蓝牙主机控制器接口（Bluetooth HCI）](#id25)

> - 引入新的HCI驱动API，并弃用旧API。（[GitHub #72323](https://github.com/zephyrproject-rtos/zephyr/issues/72323)）新API遵循常规Zephyr驱动模型，包含设备树节点等。主机通过zephyr,bt-hci chosen属性选择作为控制器的驱动实例；所有HCI驱动设备树绑定派生自共同基础绑定bt-hci.yaml。
>
> > - 采用新HCI驱动API后，不再使用zephyr,bt-uart chosen属性；UART HCI驱动改为查找自身实例节点的父设备树节点，以选择UART。
> > - 采用新HCI驱动API后，zephyr,bt-hci-ipc chosen属性仅用于控制器端；HCI驱动改为依赖compatible为zephyr,bt-hci-ipc的节点。
> > - 移除BT_NO_DRIVER Kconfig选项。HCI驱动不再由一个Kconfig choice互斥选择，而可独立启用或禁用，通常取决于各自设备树节点是否启用。
> > - 删除BT_HCI_VS_EXT，其功能并入[CONFIG_BT_HCI_VS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS)。
> > - 移除BT_HCI_VS_EVT；启用[CONFIG_BT_HCI_VS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS)时即隐含支持厂商事件。
> > - 移除bt_read_static_addr() API。它并非完全公开的API，但由于曾从公开头文件hci_driver.h导出，因此在此说明。应启用[CONFIG_BT_HCI_VS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_VS)，并通过厂商专用HCI命令API，在控制器支持时获取其蓝牙静态地址。

<a id="bluetooth-mesh"></a>

### [蓝牙网状网络（Bluetooth Mesh）](#id26)


- [bt_mesh_model](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model.html)的模型元数据指针声明增加const限定；[bt_mesh_models_metadata_entry](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__models__metadata__entry.html)的数据指针也增加const。模型元数据结构及其原始值可在非易失性存储器中声明为永久常量。（[GitHub #69679](https://github.com/zephyrproject-rtos/zephyr/issues/69679)）
- [bt_mesh_model](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model.html)的模型元数据指针声明改为单个const *，并移除[bt_mesh_health_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv.html)中的冗余元数据指针；BT_MESH_MODEL_HEALTH_SRV因此改用可变参数形式。实现支持[CONFIG_BT_MESH_LARGE_COMP_DATA_SRV](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LARGE_COMP_DATA_SRV)且需要为Health Server模型指定元数据时，将metadata作为宏的最后一个参数，否则省略。（[GitHub #71281](https://github.com/zephyrproject-rtos/zephyr/issues/71281)）

<a id="bluetooth-audio"></a>

### [蓝牙音频（Bluetooth Audio）](#id27)


- 启用[CONFIG_BT_BAP_UNICAST_SERVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_SERVER)时，不再自动启用[CONFIG_BT_ASCS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS)、[CONFIG_BT_PERIPHERAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PERIPHERAL)及[CONFIG_BT_ISO_PERIPHERAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_PERIPHERAL)；须在项目配置文件中明确设置。（[GitHub #71993](https://github.com/zephyrproject-rtos/zephyr/issues/71993)）
- CAP的发现回调bt_cap_initiator_cb.unicast_discovery_complete及bt_cap_commander_cb.discovery_complete新增集合成员（Set Member）参数。所有已定义的CAP发现回调都须增加该参数。（[GitHub #72797](https://github.com/zephyrproject-rtos/zephyr/issues/72797)）
- [bt_bap_stream_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga8f2dc67c35299334d21c7dee7b8664ae)不再连接连接等时流（CIS）。要连接CIS，须先调用[bt_bap_stream_connect()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa75f2cd2c36fdaef04a62c95bec6e2e3)，再调用[bt_bap_stream_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga8f2dc67c35299334d21c7dee7b8664ae)。（[GitHub #73032](https://github.com/zephyrproject-rtos/zephyr/issues/73032)）
- stream_lang改名为lang，以符合Assigned Numbers分配编号文档，影响BT_AUDIO_METADATA_TYPE_LANG宏及以下函数：


  - [`bt_audio_codec_cap_meta_set_lang()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga555db1eff71a3bc79a5bcb959c0198cc)
  - [`bt_audio_codec_cap_meta_get_lang()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gafb631b55b69b256c60b9cf3c7f418ff8)
  - [`bt_audio_codec_cfg_meta_set_lang()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga93052db14c857097e7cf9abc34b7fc39)
  - [`bt_audio_codec_cfg_meta_get_lang()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga55e3cbaeacf15fcb1f24a16eb28db99c)

  参见[GitHub #72584](https://github.com/zephyrproject-rtos/zephyr/issues/72584)。
- lang从uint32_t改为uint8_t [3]，影响以下函数：


  - [`bt_audio_codec_cap_meta_set_lang()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga555db1eff71a3bc79a5bcb959c0198cc)
  - [`bt_audio_codec_cap_meta_get_lang()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#gafb631b55b69b256c60b9cf3c7f418ff8)
  - [`bt_audio_codec_cfg_meta_set_lang()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga93052db14c857097e7cf9abc34b7fc39)
  - [`bt_audio_codec_cfg_meta_get_lang()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#ga55e3cbaeacf15fcb1f24a16eb28db99c)

  因此现在可用"eng"及"deu"等字符串设置新值，读取时也可避免不必要的数据复制。（[GitHub #72584](https://github.com/zephyrproject-rtos/zephyr/issues/72584)）
- 所有set_sirk都改为sirk，因为SIRK中的S本来就表示set，即集合。（[GitHub #73413](https://github.com/zephyrproject-rtos/zephyr/issues/73413)）
- [bt_audio_codec_cfg_get_chan_allocation()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gae712e0f8e84aeb4ad2528da34907e29d)新增fallback_to_default参数；如需保持已有行为，设为false。（[GitHub #72090](https://github.com/zephyrproject-rtos/zephyr/issues/72090)）
- [bt_audio_codec_cap_get_supported_audio_chan_counts()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga63d5e083f03ec06939ee1cd0355c8c2a)新增fallback_to_default参数；如需保持已有行为，设为false。（[GitHub #72090](https://github.com/zephyrproject-rtos/zephyr/issues/72090)）
- [bt_audio_codec_cap_get_max_codec_frames_per_sdu()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cap.html#ga194d938896ee65601bdce96d68c84885)新增fallback_to_default参数；如需保持已有行为，设为false。（[GitHub #72090](https://github.com/zephyrproject-rtos/zephyr/issues/72090)）
- [bt_audio_codec_cfg_meta_get_pref_context()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio__codec__cfg.html#gaea087663426a49bb6ff4859800aecb84)新增fallback_to_default参数；如需保持已有行为，设为false。（[GitHub #72090](https://github.com/zephyrproject-rtos/zephyr/issues/72090)）

<a id="bluetooth-classic"></a>

### [经典蓝牙（Bluetooth Classic）](#id28)


- 主机BR/EDR源码移到subsys/bluetooth/host/classic，头文件移到include/zephyr/bluetooth/classic。移除CONFIG_BT_BREDR，由新选项[CONFIG_BT_CLASSIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC)替代。（[GitHub #69651](https://github.com/zephyrproject-rtos/zephyr/issues/69651)）

<a id="bluetooth-host"></a>

### [蓝牙主机（Bluetooth Host）](#id29)


- 本版本弃用广播选项BT_LE_ADV_OPT_USE_NAME及BT_LE_ADV_OPT_FORCE_NAME_IN_AD。应用须明确加入设备名称，例如在传给主机的广播数据或扫描响应数据中添加以下内容：

  ```text
  BT_DATA(BT_DATA_NAME_COMPLETE, CONFIG_BT_DEVICE_NAME, sizeof(CONFIG_BT_DEVICE_NAME) - 1)
  ```

  参见[GitHub #71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)。
- 移除bt_l2cap_le_endpoint的init_credits字段，因为从Zephyr 3.4.0起已不再使用。删除所有字段引用即可，无需其他操作。
- [BT_LE_ADV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9557269dd36b624b49e76c511c3a0cc1)现在返回const指针。若将结果保存为局部变量，例如struct bt_le_adv_param *param = BT_LE_ADV_CONN;，须改为const struct bt_le_adv_param *param = BT_LE_ADV_CONN;，或用它初始化结构体，例如struct bt_le_adv_param param = *BT_LE_ADV_CONN;。

  [BT_LE_ADV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9557269dd36b624b49e76c511c3a0cc1)变更也影响所有派生宏，包括但不限于：


  - `BT_LE_ADV_CONN`
  - [`BT_LE_ADV_NCONN`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1610555bf59f1d691d640f245957fdce)
  - [`BT_LE_EXT_ADV_SCAN`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5dd57fc7f0e213db08655e631a2f314e)
  - `BT_LE_EXT_ADV_CODED_NCONN_NAME`

  参见[GitHub #75065](https://github.com/zephyrproject-rtos/zephyr/issues/75065)。
- CONFIG_BT_BUF_ACL_RX_COUNT现在必须大于[CONFIG_BT_MAX_CONN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)。由于HCI接口设计，这一约束一直存在，现在通过构建时断言强制检查。

  参见[GitHub #75592](https://github.com/zephyrproject-rtos/zephyr/issues/75592)。

<a id="bluetooth-crypto"></a>

### [蓝牙密码功能（Bluetooth Crypto）](#id30)


- 新增CONFIG_BT_USE_PSA_API，明确要求密码运算使用PSA API而非TinyCrypt。仅在系统存在PSA密码服务提供者，即设置CONFIG_PSA_CRYPTO_CLIENT时才可用。（[GitHub #73378](https://github.com/zephyrproject-rtos/zephyr/issues/73378)）

<a id="networking"></a>

## [网络（Networking）](#id31)


- 弃用旧选项CONFIG_NET_SOCKETS_POSIX_NAMES。它曾允许在不启用POSIX API时调用BSD套接字API，但会使需要启用[CONFIG_POSIX_API](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API)的应用构建复杂化。现在应用若使用常规BSD套接字接口，须启用[CONFIG_POSIX_API](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API)；若不想或不能启用，则必须为套接字API调用添加zsock_前缀。所有使用BSD套接字的示例都已改为启用[CONFIG_POSIX_API](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API)。网络栈内部不启用POSIX API，因此使用套接字的网络库已转换到zsock_* API。（[GitHub #69950](https://github.com/zephyrproject-rtos/zephyr/issues/69950)）
- zperf_results结构体的传输字节数total_len及测试时长time_in_us、client_time_in_us从32位改为64位，使长时间zperf测试能显示正确吞吐量。（[GitHub #69500](https://github.com/zephyrproject-rtos/zephyr/issues/69500)）
- 网络接口的每个IPv4地址现在各自关联IPv4子网掩码，而不再为整个接口设置一个。若接口只有一个IPv4地址，用户侧行为不变；若有多个地址，则须为每个地址单独指定掩码。（[GitHub #68419](https://github.com/zephyrproject-rtos/zephyr/issues/68419)）
- 虚拟网络接口API移除input回调。它原用于读取IP隧道内层IPv4／IPv6分组，现在隧道接收读取由recv回调实现。（[GitHub #70549](https://github.com/zephyrproject-rtos/zephyr/issues/70549)）
- 虚拟局域网VLAN实现改用虚拟网络接口。API未变，但VLAN接口类型从ETHERNET变为VIRTUAL，设置VLAN标签的代码可能需要调整。例如[net_eth_is_vlan_enabled()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac536aa7154c4a8d194ec67efb68e275c)的第二个接口参数必须指向主以太网接口，而非VLAN接口。（[GitHub #70345](https://github.com/zephyrproject-rtos/zephyr/issues/70345)）
- wifi connect命令的参数改为键值格式。以前根据参数位置识别选项，难以处理可选参数及扩展新选项；键值格式更便于扩展。执行wifi -h可查看connect用法。（[GitHub #70024](https://github.com/zephyrproject-rtos/zephyr/issues/70024)）
- 弃用CONFIG_NET_TCP_ACK_TIMEOUT。它只用于TCP握手，而该场景的总超时也应像其他情况一样由总重传超时决定，因此该配置既冗余又易混淆。改用[CONFIG_NET_TCP_INIT_RETRANSMISSION_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP_INIT_RETRANSMISSION_TIMEOUT)及[CONFIG_NET_TCP_RETRY_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP_RETRY_COUNT)控制TCP层总超时。（[GitHub #70731](https://github.com/zephyrproject-rtos/zephyr/issues/70731)）
- LwM2M API的[lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)回调类型新增offset参数，表示CoAP分块传输中的数据偏移。写后处理、验证及部分固件回调须更新以接收该参数。（[GitHub #72590](https://github.com/zephyrproject-rtos/zephyr/issues/72590)）
- DNS解析器及mDNS／LLMNR响应器改用套接字服务API，系统中可轮询套接字数量可能需要增加。确认CONFIG_NET_SOCKETS_POLL_MAX及CONFIG_POSIX_MAX_FDS足够大；具体值取决于应用需求及用法，无法给出统一数值。（[GitHub #72834](https://github.com/zephyrproject-rtos/zephyr/issues/72834)）
- 分组套接字AF_PACKET的socket API调用中，protocol字段改为网络字节序，以兼容Linux。若要接收全部网络分组，Linux要求传入htons(ETH_P_ALL)。详情见[https://www.man7.org/linux/man-pages/man7/packet.7.html](https://www.man7.org/linux/man-pages/man7/packet.7.html)。（[GitHub #73338](https://github.com/zephyrproject-rtos/zephyr/issues/73338)）
- TCP初始序列号ISN生成从MD5改用SHA-256，哈希计算的密码支持也由Mbed TLS改为PSA API。[CONFIG_NET_TCP_ISN_RFC6528](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP_ISN_RFC6528)改为依赖PSA_WANT_ALG_SHA_256，而非旧CONFIG_MBEDTLS_*功能。（[GitHub #71827](https://github.com/zephyrproject-rtos/zephyr/issues/71827)）

<a id="other-subsystems"></a>

## [其他子系统（Other Subsystems）](#id32)

<a id="flash-map"></a>

### [Flash映射（Flash Map）](#id33)


- Flash校验函数的密码后端CONFIG_FLASH_AREA_CHECK_INTEGRITY_BACKEND从TinyCrypt或Mbed TLS，改为PSA或Mbed TLS。更新后的Mbed TLS实现比此前TinyCrypt实现占用略小；对使用TF-M的设备，PSA实现可进一步减小体积。后续支持方向是PSA，但若无法承担启用PSA API的一次性开销，无TF-M设备需[CONFIG_MBEDTLS_PSA_CRYPTO_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_C)，目前仍可使用Mbed TLS。（[GitHub #73511](https://github.com/zephyrproject-rtos/zephyr/issues/73511)）

<a id="hawkbit"></a>

### [设备更新服务（hawkBit）](#id34)


- [CONFIG_HAWKBIT_PORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_PORT)由字符串改为整数。hawkBit现在用设置子系统保存配置，因此使用时必须启用[CONFIG_SETTINGS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)。（[GitHub #68806](https://github.com/zephyrproject-rtos/zephyr/issues/68806)）

<a id="mcumgr"></a>

### [微控制器管理（MCUmgr）](#id35)


- 校验和／哈希函数的SHA-256支持，从TinyCrypt或Mbed TLS改为PSA或Mbed TLS。后续推荐PSA API，但若尚未启用CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT且代码体积限制严格，改用Mbed TLS可能节省1.3 KB。

<a id="modem"></a>

### [调制解调器（Modem）](#id36)


- CONFIG_MODEM_CHAT_LOG_BUFFER重命名为[CONFIG_MODEM_CHAT_LOG_BUFFER_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CHAT_LOG_BUFFER_SIZE)。（[GitHub #70405](https://github.com/zephyrproject-rtos/zephyr/issues/70405)）

<a id="posix-api"></a>

<a id="zephyr-3-7-posix-api-migration"></a>

### [POSIX应用编程接口（POSIX API）](#id37)


- [POSIX API的Kconfig弃用项](https://docs.zephyrproject.org/latest/releases/release-notes-3.7.html#zephyr-3-7-posix-api-deprecations)可能要求修改prj.conf等配置文件，详见发行说明。也可用随附迁移脚本自动处理，运行：

  ```text
  $ python ${ZEPHYR_BASE}/scripts/utils/migrate_posix_kconfigs.py -r root_path
  ```

<a id="state-machine-framework"></a>

### [状态机框架（State Machine Framework）](#id38)


- [SMF_CREATE_STATE](../smf/P005_状态机API参考.md#ga5760b98a36ed1ac55eba700cf44c7e1e)宏现在始终接收5个参数，不再取决于[CONFIG_SMF_ANCESTOR_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SMF_ANCESTOR_SUPPORT)及[CONFIG_SMF_INITIAL_TRANSITION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SMF_INITIAL_TRANSITION)。不使用附加参数时必须设为NULL。（[GitHub #71250](https://github.com/zephyrproject-rtos/zephyr/issues/71250)）
- 当转换源是[smf_run_state()](../smf/P005_状态机API参考.md#ga8399cfa9e793a7f188b4ed4fec9f4f90)所执行状态的父状态时，SMF现在采用更符合UML的转换流程：执行退出动作，直到转换源与目标状态的最低共同祖先LCA，但不包含LCA；再从LCA向下执行进入动作到目标状态，同样不包含LCA。（[GitHub #71675](https://github.com/zephyrproject-rtos/zephyr/issues/71675)）
- 以前以new_state=NULL调用[smf_set_state()](../smf/P005_状态机API参考.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)，会执行从当前状态到最顶层父状态的所有退出动作，并期望最顶层退出动作终止状态机。现在禁止传NULL。应改为在顶层创建终止状态，并从其进入动作调用[smf_set_terminate()](../smf/P005_状态机API参考.md#gaae28c66f0652c99ba8e843eeaf02aaf7)。

<a id="updatehub"></a>

### [固件更新服务（UpdateHub）](#id39)


- 完整性检查使用的SHA-256实现不再由CONFIG_FLASH_AREA_CHECK_INTEGRITY_BACKEND选择，而根据CONFIG_PSA_CRYPTO_CLIENT在Mbed TLS及PSA间选择。除非开发板使用TF-M或启用[CONFIG_MBEDTLS_PSA_CRYPTO_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_C)，否则仍默认采用体积比以前更小的Mbed TLS实现。（[GitHub #73511](https://github.com/zephyrproject-rtos/zephyr/issues/73511)）

<a id="architectures"></a>

## [架构（Architectures）](#id40)


- arch_start_cpu()重命名为[arch_cpu_start()](../arch_core_reference/P005_架构多处理器接口.md#ga32b7e543ce51498200c368c39c900bc8)。（[GitHub #64987](https://github.com/zephyrproject-rtos/zephyr/issues/64987)）
- 弃用CONFIG_ARM64_ENABLE_FRAME_POINTER，改用[CONFIG_FRAME_POINTER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FRAME_POINTER)。（[GitHub #72646](https://github.com/zephyrproject-rtos/zephyr/issues/72646)）
- x86


  - 弃用CONFIG_DISABLE_SSBD及CONFIG_ENABLE_EXTENDED_IBRS，改用[CONFIG_X86_DISABLE_SSBD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_DISABLE_SSBD)及[CONFIG_X86_ENABLE_EXTENDED_IBRS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_ENABLE_EXTENDED_IBRS)。（[GitHub #69690](https://github.com/zephyrproject-rtos/zephyr/issues/69690)）
- POSIX架构（POSIX Arch）：


  - 重构LLVM模糊测试支持。测试应用现在须自己提供LLVMFuzzerTestOneInput()钩子，不再依赖开发板提供；示例见samples/subsys/debug/fuzz/。（[GitHub #71378](https://github.com/zephyrproject-rtos/zephyr/issues/71378)）

## 译注

配置、API、时钟和签名算法变化均按3.6到3.7的迁移方向解释；源码示例保留原文。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：版本发布与维护](P002_版本发布与维护.md) · [本模块主线目录](../reading/releases_guides.md) · [全部主线](../reading/README.md) · [下一篇：迁移到Zephyr 4.2](P004_迁移到Zephyr_4.2.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P002_版本发布与维护.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_迁移到Zephyr_4.2.md)

</details>

<!-- reading-navigation:end -->
