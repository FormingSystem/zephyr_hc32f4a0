---
id: learning.zephyr-docs.api-file-reference.page-516
title: zephyr__dt-bindings__pinctrl__xmc4xxx-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xmc4xxx-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第516章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_xmc4xxx-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/xmc4xxx-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 516.1\_宏定义（Macros）

<a id="r_aab30618ebe31012b3bf6a72d55f9335c"></a>

```c
#define XMC4XXX_PORT_POS 0
```

相关声明：[XMC4XXX_PORT_POS](#aab30618ebe31012b3bf6a72d55f9335c)。

<a id="r_a99aa017fa346da406fca137d0c42c1e4"></a>

```c
#define XMC4XXX_PORT_MASK 0xf
```

相关声明：[XMC4XXX_PORT_MASK](#a99aa017fa346da406fca137d0c42c1e4)。

<a id="r_a511179d787ebfbb7f37a92326d4a8984"></a>

```c
#define XMC4XXX_PIN_POS 4
```

相关声明：[XMC4XXX_PIN_POS](#a511179d787ebfbb7f37a92326d4a8984)。

<a id="r_a693fe19f7d6073121d89c4bd6dbff99b"></a>

```c
#define XMC4XXX_PIN_MASK 0xf
```

相关声明：[XMC4XXX_PIN_MASK](#a693fe19f7d6073121d89c4bd6dbff99b)。

<a id="r_a532151552d5ea717d093deb4c9c9d233"></a>

```c
#define XMC4XXX_ALT_POS 8
```

相关声明：[XMC4XXX_ALT_POS](#a532151552d5ea717d093deb4c9c9d233)。

<a id="r_aba9bea82a961c304cb90a7c24527d531"></a>

```c
#define XMC4XXX_ALT_MASK 0xf
```

相关声明：[XMC4XXX_ALT_MASK](#aba9bea82a961c304cb90a7c24527d531)。

<a id="r_ac6ec7a70bdaae2909baea4f179327871"></a>

```c
#define XMC4XXX_PULL_DOWN_POS 12
```

相关声明：[XMC4XXX_PULL_DOWN_POS](#ac6ec7a70bdaae2909baea4f179327871)。

<a id="r_ac202c2ad9b97865b1d7f9d282c9a7d10"></a>

```c
#define XMC4XXX_PULL_DOWN_MASK 0x1
```

相关声明：[XMC4XXX_PULL_DOWN_MASK](#ac202c2ad9b97865b1d7f9d282c9a7d10)。

<a id="r_a87e81f7624a28d5fea5ad3a2074329a0"></a>

```c
#define XMC4XXX_PULL_UP_POS 13
```

相关声明：[XMC4XXX_PULL_UP_POS](#a87e81f7624a28d5fea5ad3a2074329a0)。

<a id="r_ac165407103a525da4919fee7c4dc22c9"></a>

```c
#define XMC4XXX_PULL_UP_MASK 0x1
```

相关声明：[XMC4XXX_PULL_UP_MASK](#ac165407103a525da4919fee7c4dc22c9)。

<a id="r_a9f50c28d310a0cc771b979e731c05060"></a>

```c
#define XMC4XXX_PUSH_PULL_POS 14
```

相关声明：[XMC4XXX_PUSH_PULL_POS](#a9f50c28d310a0cc771b979e731c05060)。

<a id="r_a308fe5c756b2058b2eec25d9e95d439a"></a>

```c
#define XMC4XXX_PUSH_PULL_MASK 0x1
```

相关声明：[XMC4XXX_PUSH_PULL_MASK](#a308fe5c756b2058b2eec25d9e95d439a)。

<a id="r_ad8da22497d5f36d3cd56477506eca3b5"></a>

```c
#define XMC4XXX_OPEN_DRAIN_POS 15
```

相关声明：[XMC4XXX_OPEN_DRAIN_POS](#ad8da22497d5f36d3cd56477506eca3b5)。

<a id="r_a4dbdbb0b4fe95db634c55b7840a08a47"></a>

```c
#define XMC4XXX_OPEN_DRAIN_MASK 0x1
```

相关声明：[XMC4XXX_OPEN_DRAIN_MASK](#a4dbdbb0b4fe95db634c55b7840a08a47)。

<a id="r_ada9fafd51a6d8e7e6b4f2b05bf2d3dd0"></a>

```c
#define XMC4XXX_OUT_HIGH_POS 16
```

相关声明：[XMC4XXX_OUT_HIGH_POS](#ada9fafd51a6d8e7e6b4f2b05bf2d3dd0)。

<a id="r_a58396a809d6950afd8b5cc6fd4193589"></a>

```c
#define XMC4XXX_OUT_HIGH_MASK 0x1
```

相关声明：[XMC4XXX_OUT_HIGH_MASK](#a58396a809d6950afd8b5cc6fd4193589)。

<a id="r_abbac18ae6e6d52b33db5b352ca323e11"></a>

```c
#define XMC4XXX_OUT_LOW_POS 17
```

相关声明：[XMC4XXX_OUT_LOW_POS](#abbac18ae6e6d52b33db5b352ca323e11)。

<a id="r_af8c9d1c2e5664ff59538c08b4ed8fa8b"></a>

```c
#define XMC4XXX_OUT_LOW_MASK 0x1
```

相关声明：[XMC4XXX_OUT_LOW_MASK](#af8c9d1c2e5664ff59538c08b4ed8fa8b)。

<a id="r_a2da9db848ad0c85751747df0f3948f97"></a>

```c
#define XMC4XXX_INV_INPUT_POS 18
```

相关声明：[XMC4XXX_INV_INPUT_POS](#a2da9db848ad0c85751747df0f3948f97)。

<a id="r_aab423e91fbddbe908d9393447ff943f0"></a>

```c
#define XMC4XXX_INV_INPUT_MASK 0x1
```

相关声明：[XMC4XXX_INV_INPUT_MASK](#aab423e91fbddbe908d9393447ff943f0)。

<a id="r_ac8284e39124ff71b5335e46e56fb8000"></a>

```c
#define XMC4XXX_DRIVE_POS 19
```

相关声明：[XMC4XXX_DRIVE_POS](#ac8284e39124ff71b5335e46e56fb8000)。

<a id="r_aa6829bced6bf9f7908e31fb3c9205f93"></a>

```c
#define XMC4XXX_DRIVE_MASK 0x7
```

相关声明：[XMC4XXX_DRIVE_MASK](#aa6829bced6bf9f7908e31fb3c9205f93)。

<a id="r_a80e80262f3abb20055891211ee43201a"></a>

```c
#define XMC4XXX_HWCTRL_POS 22
```

相关声明：[XMC4XXX_HWCTRL_POS](#a80e80262f3abb20055891211ee43201a)。

<a id="r_a0fc560c059b8fabf8e811e81783f5e2a"></a>

```c
#define XMC4XXX_HWCTRL_MASK 0x3
```

相关声明：[XMC4XXX_HWCTRL_MASK](#a0fc560c059b8fabf8e811e81783f5e2a)。

<a id="r_a30211ecff4f4b6b3f02386ae55d1cb8d"></a>

```c
#define XMC4XXX_PINMUX_SET(port, pin, alt_fun)
```

相关声明：[XMC4XXX_PINMUX_SET](#a30211ecff4f4b6b3f02386ae55d1cb8d)。

<a id="r_ae0748e6dbb9ca36ad0ab40e3a53daea2"></a>

```c
#define XMC4XXX_PINMUX_GET_PORT(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_PORT](#ae0748e6dbb9ca36ad0ab40e3a53daea2)。

<a id="r_a3d889d7f75a6b88b252cb13f3004ea6a"></a>

```c
#define XMC4XXX_PINMUX_GET_PIN(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_PIN](#a3d889d7f75a6b88b252cb13f3004ea6a)。

<a id="r_afdad7ccafbdee5a2b1d512f0e280abfe"></a>

```c
#define XMC4XXX_PINMUX_GET_ALT(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_ALT](#afdad7ccafbdee5a2b1d512f0e280abfe)。

<a id="r_a56ebba3de971f70ad47005cf0a5246c1"></a>

```c
#define XMC4XXX_PINMUX_GET_PULL_DOWN(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_PULL_DOWN](#a56ebba3de971f70ad47005cf0a5246c1)。

<a id="r_ac28a73b740da97d7d0008ab0af577a92"></a>

```c
#define XMC4XXX_PINMUX_GET_PULL_UP(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_PULL_UP](#ac28a73b740da97d7d0008ab0af577a92)。

<a id="r_a376e85562e0dc5a1ea2c9f3b8eaeeb9e"></a>

```c
#define XMC4XXX_PINMUX_GET_PUSH_PULL(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_PUSH_PULL](#a376e85562e0dc5a1ea2c9f3b8eaeeb9e)。

<a id="r_a57626f3b88704a87ed5f9bfba44c8daf"></a>

```c
#define XMC4XXX_PINMUX_GET_OPEN_DRAIN(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_OPEN_DRAIN](#a57626f3b88704a87ed5f9bfba44c8daf)。

<a id="r_a1de2bc4e89167d9a0399edf63078d928"></a>

```c
#define XMC4XXX_PINMUX_GET_OUT_HIGH(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_OUT_HIGH](#a1de2bc4e89167d9a0399edf63078d928)。

<a id="r_abbeef6122d273c9f074fb1cc5456febf"></a>

```c
#define XMC4XXX_PINMUX_GET_OUT_LOW(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_OUT_LOW](#abbeef6122d273c9f074fb1cc5456febf)。

<a id="r_a43ce0d809351bef0989f0330073f9453"></a>

```c
#define XMC4XXX_PINMUX_GET_INV_INPUT(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_INV_INPUT](#a43ce0d809351bef0989f0330073f9453)。

<a id="r_a11bd50351e3aabed088cc4158474edc3"></a>

```c
#define XMC4XXX_PINMUX_GET_DRIVE(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_DRIVE](#a11bd50351e3aabed088cc4158474edc3)。

<a id="r_a33694b664b4212d95cc18659173675c0"></a>

```c
#define XMC4XXX_PINMUX_GET_HWCTRL(mx)
```

相关声明：[XMC4XXX_PINMUX_GET_HWCTRL](#a33694b664b4212d95cc18659173675c0)。

## 516.2\_详细说明（Detailed Documentation）

<a id="aba9bea82a961c304cb90a7c24527d531"></a>

### `XMC4XXX_ALT_MASK`

```c
#define XMC4XXX_ALT_MASK 0xf
```

<a id="a532151552d5ea717d093deb4c9c9d233"></a>

### `XMC4XXX_ALT_POS`

```c
#define XMC4XXX_ALT_POS 8
```

<a id="aa6829bced6bf9f7908e31fb3c9205f93"></a>

### `XMC4XXX_DRIVE_MASK`

```c
#define XMC4XXX_DRIVE_MASK 0x7
```

<a id="ac8284e39124ff71b5335e46e56fb8000"></a>

### `XMC4XXX_DRIVE_POS`

```c
#define XMC4XXX_DRIVE_POS 19
```

<a id="a0fc560c059b8fabf8e811e81783f5e2a"></a>

### `XMC4XXX_HWCTRL_MASK`

```c
#define XMC4XXX_HWCTRL_MASK 0x3
```

<a id="a80e80262f3abb20055891211ee43201a"></a>

### `XMC4XXX_HWCTRL_POS`

```c
#define XMC4XXX_HWCTRL_POS 22
```

<a id="aab423e91fbddbe908d9393447ff943f0"></a>

### `XMC4XXX_INV_INPUT_MASK`

```c
#define XMC4XXX_INV_INPUT_MASK 0x1
```

<a id="a2da9db848ad0c85751747df0f3948f97"></a>

### `XMC4XXX_INV_INPUT_POS`

```c
#define XMC4XXX_INV_INPUT_POS 18
```

<a id="a4dbdbb0b4fe95db634c55b7840a08a47"></a>

### `XMC4XXX_OPEN_DRAIN_MASK`

```c
#define XMC4XXX_OPEN_DRAIN_MASK 0x1
```

<a id="ad8da22497d5f36d3cd56477506eca3b5"></a>

### `XMC4XXX_OPEN_DRAIN_POS`

```c
#define XMC4XXX_OPEN_DRAIN_POS 15
```

<a id="a58396a809d6950afd8b5cc6fd4193589"></a>

### `XMC4XXX_OUT_HIGH_MASK`

```c
#define XMC4XXX_OUT_HIGH_MASK 0x1
```

<a id="ada9fafd51a6d8e7e6b4f2b05bf2d3dd0"></a>

### `XMC4XXX_OUT_HIGH_POS`

```c
#define XMC4XXX_OUT_HIGH_POS 16
```

<a id="af8c9d1c2e5664ff59538c08b4ed8fa8b"></a>

### `XMC4XXX_OUT_LOW_MASK`

```c
#define XMC4XXX_OUT_LOW_MASK 0x1
```

<a id="abbac18ae6e6d52b33db5b352ca323e11"></a>

### `XMC4XXX_OUT_LOW_POS`

```c
#define XMC4XXX_OUT_LOW_POS 17
```

<a id="a693fe19f7d6073121d89c4bd6dbff99b"></a>

### `XMC4XXX_PIN_MASK`

```c
#define XMC4XXX_PIN_MASK 0xf
```

<a id="a511179d787ebfbb7f37a92326d4a8984"></a>

### `XMC4XXX_PIN_POS`

```c
#define XMC4XXX_PIN_POS 4
```

<a id="afdad7ccafbdee5a2b1d512f0e280abfe"></a>

### `XMC4XXX_PINMUX_GET_ALT`

```c
#define XMC4XXX_PINMUX_GET_ALT ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_ALT_POS)        & XMC4XXX_ALT_MASK)
```

<a id="a11bd50351e3aabed088cc4158474edc3"></a>

### `XMC4XXX_PINMUX_GET_DRIVE`

```c
#define XMC4XXX_PINMUX_GET_DRIVE ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_DRIVE_POS)      & XMC4XXX_DRIVE_MASK)
```

<a id="a33694b664b4212d95cc18659173675c0"></a>

### `XMC4XXX_PINMUX_GET_HWCTRL`

```c
#define XMC4XXX_PINMUX_GET_HWCTRL ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_HWCTRL_POS)     & XMC4XXX_HWCTRL_MASK)
```

<a id="a43ce0d809351bef0989f0330073f9453"></a>

### `XMC4XXX_PINMUX_GET_INV_INPUT`

```c
#define XMC4XXX_PINMUX_GET_INV_INPUT ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_INV_INPUT_POS)  & XMC4XXX_INV_INPUT_MASK)
```

<a id="a57626f3b88704a87ed5f9bfba44c8daf"></a>

### `XMC4XXX_PINMUX_GET_OPEN_DRAIN`

```c
#define XMC4XXX_PINMUX_GET_OPEN_DRAIN ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_OPEN_DRAIN_POS) & XMC4XXX_OPEN_DRAIN_MASK)
```

<a id="a1de2bc4e89167d9a0399edf63078d928"></a>

### `XMC4XXX_PINMUX_GET_OUT_HIGH`

```c
#define XMC4XXX_PINMUX_GET_OUT_HIGH ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_OUT_HIGH_POS)   & XMC4XXX_OUT_HIGH_MASK)
```

<a id="abbeef6122d273c9f074fb1cc5456febf"></a>

### `XMC4XXX_PINMUX_GET_OUT_LOW`

```c
#define XMC4XXX_PINMUX_GET_OUT_LOW ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_OUT_LOW_POS)    & XMC4XXX_OUT_LOW_MASK)
```

<a id="a3d889d7f75a6b88b252cb13f3004ea6a"></a>

### `XMC4XXX_PINMUX_GET_PIN`

```c
#define XMC4XXX_PINMUX_GET_PIN ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_PIN_POS)        & XMC4XXX_PIN_MASK)
```

<a id="ae0748e6dbb9ca36ad0ab40e3a53daea2"></a>

### `XMC4XXX_PINMUX_GET_PORT`

```c
#define XMC4XXX_PINMUX_GET_PORT ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_PORT_POS)       & XMC4XXX_PORT_MASK)
```

<a id="a56ebba3de971f70ad47005cf0a5246c1"></a>

### `XMC4XXX_PINMUX_GET_PULL_DOWN`

```c
#define XMC4XXX_PINMUX_GET_PULL_DOWN ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_PULL_DOWN_POS)  & XMC4XXX_PULL_DOWN_MASK)
```

<a id="ac28a73b740da97d7d0008ab0af577a92"></a>

### `XMC4XXX_PINMUX_GET_PULL_UP`

```c
#define XMC4XXX_PINMUX_GET_PULL_UP ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_PULL_UP_POS)    & XMC4XXX_PULL_UP_MASK)
```

<a id="a376e85562e0dc5a1ea2c9f3b8eaeeb9e"></a>

### `XMC4XXX_PINMUX_GET_PUSH_PULL`

```c
#define XMC4XXX_PINMUX_GET_PUSH_PULL ( mx)
```

展开值（Value）：

```c
((mx >> XMC4XXX_PUSH_PULL_POS)  & XMC4XXX_PUSH_PULL_MASK)
```

<a id="a30211ecff4f4b6b3f02386ae55d1cb8d"></a>

### `XMC4XXX_PINMUX_SET`

```c
#define XMC4XXX_PINMUX_SET ( port, pin, alt_fun )
```

展开值（Value）：

```c
((port) << XMC4XXX_PORT_POS | (pin) << XMC4XXX_PIN_POS | (alt_fun) << XMC4XXX_ALT_POS)
```

<a id="a99aa017fa346da406fca137d0c42c1e4"></a>

### `XMC4XXX_PORT_MASK`

```c
#define XMC4XXX_PORT_MASK 0xf
```

<a id="aab30618ebe31012b3bf6a72d55f9335c"></a>

### `XMC4XXX_PORT_POS`

```c
#define XMC4XXX_PORT_POS 0
```

<a id="ac202c2ad9b97865b1d7f9d282c9a7d10"></a>

### `XMC4XXX_PULL_DOWN_MASK`

```c
#define XMC4XXX_PULL_DOWN_MASK 0x1
```

<a id="ac6ec7a70bdaae2909baea4f179327871"></a>

### `XMC4XXX_PULL_DOWN_POS`

```c
#define XMC4XXX_PULL_DOWN_POS 12
```

<a id="ac165407103a525da4919fee7c4dc22c9"></a>

### `XMC4XXX_PULL_UP_MASK`

```c
#define XMC4XXX_PULL_UP_MASK 0x1
```

<a id="a87e81f7624a28d5fea5ad3a2074329a0"></a>

### `XMC4XXX_PULL_UP_POS`

```c
#define XMC4XXX_PULL_UP_POS 13
```

<a id="a308fe5c756b2058b2eec25d9e95d439a"></a>

### `XMC4XXX_PUSH_PULL_MASK`

```c
#define XMC4XXX_PUSH_PULL_MASK 0x1
```

<a id="a9f50c28d310a0cc771b979e731c05060"></a>

### `XMC4XXX_PUSH_PULL_POS`

```c
#define XMC4XXX_PUSH_PULL_POS 14
```


## 516.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P126_xmc4xxx-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="axmc4xxx-pinctrl_8h_html_a532151552d5ea717d093deb4c9c9d233"></a>
<a id="axmc4xxx-pinctrl_8h_html_aba9bea82a961c304cb90a7c24527d531"></a>
<a id="axmc4xxx-pinctrl_8h_html_aa6829bced6bf9f7908e31fb3c9205f93"></a>
<a id="axmc4xxx-pinctrl_8h_html_ac8284e39124ff71b5335e46e56fb8000"></a>
<a id="axmc4xxx-pinctrl_8h_html_a0fc560c059b8fabf8e811e81783f5e2a"></a>
<a id="axmc4xxx-pinctrl_8h_html_a80e80262f3abb20055891211ee43201a"></a>
<a id="axmc4xxx-pinctrl_8h_html_a2da9db848ad0c85751747df0f3948f97"></a>
<a id="axmc4xxx-pinctrl_8h_html_aab423e91fbddbe908d9393447ff943f0"></a>
<a id="axmc4xxx-pinctrl_8h_html_a4dbdbb0b4fe95db634c55b7840a08a47"></a>
<a id="axmc4xxx-pinctrl_8h_html_ad8da22497d5f36d3cd56477506eca3b5"></a>
<a id="axmc4xxx-pinctrl_8h_html_a58396a809d6950afd8b5cc6fd4193589"></a>
<a id="axmc4xxx-pinctrl_8h_html_ada9fafd51a6d8e7e6b4f2b05bf2d3dd0"></a>
<a id="axmc4xxx-pinctrl_8h_html_abbac18ae6e6d52b33db5b352ca323e11"></a>
<a id="axmc4xxx-pinctrl_8h_html_af8c9d1c2e5664ff59538c08b4ed8fa8b"></a>
<a id="axmc4xxx-pinctrl_8h_html_a511179d787ebfbb7f37a92326d4a8984"></a>
<a id="axmc4xxx-pinctrl_8h_html_a693fe19f7d6073121d89c4bd6dbff99b"></a>
<a id="axmc4xxx-pinctrl_8h_html_a99aa017fa346da406fca137d0c42c1e4"></a>
<a id="axmc4xxx-pinctrl_8h_html_aab30618ebe31012b3bf6a72d55f9335c"></a>
<a id="axmc4xxx-pinctrl_8h_html_ac202c2ad9b97865b1d7f9d282c9a7d10"></a>
<a id="axmc4xxx-pinctrl_8h_html_ac6ec7a70bdaae2909baea4f179327871"></a>
<a id="axmc4xxx-pinctrl_8h_html_a87e81f7624a28d5fea5ad3a2074329a0"></a>
<a id="axmc4xxx-pinctrl_8h_html_ac165407103a525da4919fee7c4dc22c9"></a>
<a id="axmc4xxx-pinctrl_8h_html_a308fe5c756b2058b2eec25d9e95d439a"></a>
<a id="axmc4xxx-pinctrl_8h_html_a9f50c28d310a0cc771b979e731c05060"></a>

---

[上一章](P515_zephyr__dt-bindings__ethernet__xlnx_gem.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P517_____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest.h_文件参考.md)
