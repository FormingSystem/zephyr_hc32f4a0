---
id: learning.zephyr-docs.basic_samples.page-57
title: FIDO2认证器示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/authentication/fido2/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="fido2"></a>

# 第57章\_FIDO2认证器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/authentication/fido2/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/authentication/fido2/README.rst/..)。

<a id="overview"></a>

## 57.1 概述（Overview）

本示例将Zephyr支持的开发板变为FIDO2硬件安全密钥（Hardware Security Key）。它通过USB人机接口设备（Human Interface Device，HID）传输实现客户端到认证器协议（Client to Authenticator Protocol）CTAP2.1，即CTAPHID，并可选择支持蓝牙低功耗（Bluetooth Low Energy，Bluetooth LE）传输。

nRF54LM20的板配置同时启用USB HID和Bluetooth LE，两种传输可同时使用。其他受支持的板配置只使用USB HID。

本示例可以在支持WebAuthn的网站上进行无密码认证（Passwordless Authentication），例如[webauthn.io](https://webauthn.io)。

支持的操作包括：

- 创建凭据：`authenticatorMakeCredential`。
- 获取认证断言：`authenticatorGetAssertion`。
- 获取认证器信息：`authenticatorGetInfo`。
- 客户端PIN操作：`authenticatorClientPIN`。
- 获取下一个认证断言：`authenticatorGetNextAssertion`。
- 选择认证器：`authenticatorSelection`。

<a id="bluetooth-low-energy"></a>

### 57.1.1 蓝牙低功耗（Bluetooth Low Energy）

使用Bluetooth LE传输时，客户端必须先与认证器配对（Pair），然后才能使用FIDO2操作。

为简化示例，应用运行期间始终保持可发现（Discoverable）和可配对（Pairable）。生产应用应把新的配对限制在由用户明确启动的配对模式中。

使用WebAuthn客户端测试时，Bluetooth LE操作可能比USB HID操作更慢，因为蓝牙连接可能在两次操作之间断开并重新建立。

<a id="requirements"></a>

## 57.2 要求（Requirements）

使用USB HID需要开发板支持USB设备功能。原文称已在以下开发板上测试：

- Black Pill STM32H523：`blackpill_h523ce`。
- STM32WB55 Core Board：`weact_stm32wb55_core`。
- ESP32-S3-B：`weact_esp32s3_b/esp32s3/procpu`。
- nRF54LM20DK：`nrf54lm20dk/nrf54lm20a/cpuapp`。

使用Bluetooth LE需要开发板支持蓝牙外设（Bluetooth Peripheral）角色。原文称已在以下板上测试：

- nRF54LM20DK：`nrf54lm20dk/nrf54lm20a/cpuapp`。

用户在场（User Presence）通过按下chosen属性`zephyr,fido2-up-button`所选择的按钮确认；如果没有该选择，则回退到别名`sw0`对应的按钮。

可以通过别名`led0`对应的LED监视FIDO2运行时状态（Runtime State）。子系统暴露运行时状态，示例据此控制LED：

- LED熄灭：FIDO2空闲或已停止。
- LED闪烁：正在等待用户在场确认。
- LED常亮：正在处理请求。

> 译注——用户在场输入的版本差异：以上按钮选择规则按网页保留。当前官方用户在场后端使用输入子系统（Input Subsystem），通过chosen属性`zephyr,fido2-up-input`绑定输入设备；当前示例板覆盖文件也使用这一属性。不能把旧的`zephyr,fido2-up-button`及`sw0`回退说明直接当作当前后端的配置接口。应对照所用版本的设备树与`FIDO2_UP_INPUT`实现。

<a id="building-and-running"></a>

## 57.3 构建与运行（Building and Running）

以Black Pill STM32H523开发板为例：

> 译注——命令前提：在已准备Zephyr开发依赖、相应工具链和烧录工具的UCRT64 Bash或Linux Bash中，以Zephyr源码根目录执行。构建成功后再烧录；构建失败先检查板目标、USB与输入配置，烧录失败先检查工具和连接。本文没有烧录开发板，也没有在网站注册凭据。

```sh
# From the root of the zephyr repository
west build -b blackpill_h523ce samples/subsys/authentication/fido2
west flash
```

烧录后，通过开发板USB端口连接计算机。在任意兼容WebAuthn的浏览器中打开[webauthn.io](https://webauthn.io)，例如Chrome、Edge、Firefox或Safari，然后执行以下步骤：

1. 输入用户名，点击注册（Register）。
2. 浏览器提示使用安全密钥时，按下开发板上的用户在场按钮。
3. 如果出现提示，设置或输入个人识别码（Personal Identification Number，PIN）。
4. 注册应当成功。
5. 点击认证（Authenticate），再次按下按钮，并输入PIN登录。

> 译注——验证范围：当前控制台测试以出现`FIDO2 authenticator ready`为通过条件，这只验证应用到达就绪状态，不能代替上述浏览器注册与认证流程。另有仅构建的无USB测试，使用`CONFIG_FIDO2_UP_ALWAYS`绕过用户在场确认；它是测试配置，不代表按钮确认已验证。本文保留官方操作步骤，没有生成或使用实际网站凭据。

<a id="see-also"></a>

## 57.4 另请参阅（See also）

- [FIDO2 API](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html)。


> 译注——实现依据：[samples/subsys/authentication/fido2/tests.yaml](../../../samples/subsys/authentication/fido2/tests.yaml)、[samples/subsys/authentication/fido2/Kconfig.bt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/authentication/fido2/Kconfig.bt)、[subsys/authentication/fido2/up/Kconfig](../../../subsys/authentication/fido2/up/Kconfig)、[subsys/authentication/fido2/up/fido2_up_input.c](../../../subsys/authentication/fido2/up/fido2_up_input.c)。仓库内参照使用相对链接；官方main快照与本地版本可能不同，所核对文件的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/subsys/authentication/fido2/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/authentication/fido2/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/authentication/fido2/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/subsys/authentication/fido2/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P056_身份认证示例目录.md) · [返回大纲](大纲.md) · [下一章](P058_LoRaWAN示例目录.md)
