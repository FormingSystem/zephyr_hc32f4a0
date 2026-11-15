---
id: learning.zephyr-docs.bluetooth.page-40
title: HFP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/hfp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-classic-hfp-shell"></a>

# 第40章\_HFP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/hfp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

> 译注——术语：ACL 为异步面向连接链路（Asynchronous Connection-oriented Link）；SLC 为服务级连接（Service Level Connection）；SCO 为同步面向连接（Synchronous Connection-Oriented）链路。后文分角色展示呼叫控制和音频连接日志。

本文说明如何运行经典蓝牙（Bluetooth Classic）的免提配置文件（Hands-Free Profile，HFP）功能。`hfp` 命令提供经典蓝牙 HFP Shell 命令。

有两个子命令：`hfp hf` 和 `hfp ag`。

`hfp hf` 提供免提端（Hands-Free，HF）功能，`hfp ag` 提供音频网关（Audio Gateway，AG）功能。

<a id="commands"></a>

## 40.1 命令（Commands）

除了 `hfp hf reg` 和 `hfp ag reg`，其余命令都只能在建立 ACL 连接后使用。

`hfp` 命令如下：

```text
uart:~$ hfp
hfp - Bluetooth HFP shell commands
Subcommands:
  hf  : HFP HF shell commands
  ag  : HFP AG shell commands
```

`hfp hf` 命令如下：

```text
uart:~$ hfp hf
hf - HFP HF shell commands
Subcommands:
  reg                          : [none]
  connect                      : <channel>
  disconnect                   : [none]
  sco_disconnect               : [none]
  cli                          : <enable/disable>
  vgm                          : <gain>
  vgs                          : <gain>
  operator                     : [none]
  audio_connect                : [none]
  auto_select_codec            : <enable/disable>
  select_codec                 : Codec ID
  set_codecs                   : Codec ID Map
  accept                       : <call index>
  reject                       : <call index>
  terminate                    : <call index>
  hold_incoming                : <call index>
  query_respond_hold_status    : [none]
  number_call                  : <phone number>
  memory_dial                  : <memory location>
  redial                       : [none]
  turn_off_ecnr                : [none]
  call_waiting_notify          : <enable/disable>
  release_all_held             : [none]
  set_udub                     : [none]
  release_active_accept_other  : [none]
  hold_active_accept_other     : [none]
  join_conversation            : [none]
  explicit_call_transfer       : [none]
  release_specified_call       : <call index>
  private_consultation_mode    : <call index>
  voice_recognition            : <activate/deactivate>
  ready_to_accept_audio        : [none]
  request_phone_number         : [none]
  transmit_dtmf_code           : <call index> <code(set 0-9, #,*,A-D)>
  query_subscriber             : [none]
  indicator_status             : <Activate/deactivate AG indicators bitmap>
  enhanced_safety              : <enable/disable>
  battery                      : <level>
```

`hfp ag` 命令如下：

```text
uart:~$ hfp ag
ag - HFP AG shell commands
Subcommands:
  reg                     : [none]
  connect                 : <channel>
  disconnect              : [none]
  sco_disconnect          : [none]
  ongoing_calls           : <yes or no>
  set_ongoing_calls       : <number> <type> <status> <dir> [all]
  remote_incoming         : <number>
  hold_incoming           : <number>
  remote_reject           : <call index>
  remote_accept           : <call index>
  remote_terminate        : <call index>
  remote_ringing          : <call index>
  outgoing                : <number>
  reject                  : <call index>
  accept                  : <call index>
  hold                    : <call index>
  retrieve                : <call index>
  terminate               : <call index>
  vgm                     : <gain>
  vgs                     : <gain>
  operator                : <mode> <operator>
  audio_connect           : <codec id>
  inband_ringtone         : <enable/disable>
  explicit_call_transfer  : [none]
  voice_recognition       : <activate/deactivate>
  vre_state               : <[R-ready][S-send][P-processing]>
  vre_text                : <[R-ready][S-send][P-processing]> <id> <type>
                            <operation> <text string>
  subscriber              : <empty/notempty>
  signal_strength         : <signal strength>
  roaming_status          : <roaming status>
  battery_level           : <battery level>
  service_availability    : <yes/no>
  hf_indicator            : <indicator> <enable/disable>
```

<a id="hfp-ag-slc"></a>

## 40.2 HFP 音频网关的服务级连接（HFP AG SLC）

`hfp ag` 子命令提供经典蓝牙 HFP 音频网关功能。

注册 HFP AG：

```text
uart:~$ hfp ag reg
```

连接 HFP HF：

```text
uart:~$ hfp ag connect 1
```

已与 HF 设备建立连接：

```text
Security changed: XX:XX:XX:XX:XX:XX level 2
AG received codec id bit map 2
AG connected
AG received vgm 0
AG received vgs 0
```

断开与 HFP HF 的连接：

```text
uart:~$ hfp ag disconnect
```

连接已断开：

```text
AG disconnected
```

<a id="hfp-hf-slc"></a>

## 40.3 HFP 免提端的服务级连接（HFP HF SLC）

`hfp hf` 子命令提供经典蓝牙 HFP 免提端功能。

注册 HFP HF：

```text
uart:~$ hfp hf reg
```

连接 HFP AG：

```text
uart:~$ hfp hf connect 2
```

已与 AG 设备建立连接：

```text
Security changed: XX:XX:XX:XX:XX:XX level 2
HF service 0
HF signal 0
HF roam 0
HF battery 0
HF ring: in-band
HF connected
```

断开与 HFP HF 的连接：

```text
uart:~$ hfp hf disconnect
```

> 译注——原文角色名称：这一处原说明写作“Disconnect from HFP HF”，上方按原文保留；但本小节在 HF 端执行 `hfp hf disconnect`，实际断开的是与 AG 的连接。服务级连接（Service Level Connection，SLC）与后续音频连接是不同阶段。

连接已断开：

```text
HF disconnected
```

<a id="call-outgoing"></a>

## 40.4 呼出电话（Call outgoing）

使用 AG 提供的电话号码发起呼叫：

**AG 端的呼出时序（Outgoing Call Sequence on AG side）**

<a id="tab-0-T3V0Z29pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBBRyBzaWRl"></a>
<a id="panel-0-T3V0Z29pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBBRyBzaWRl"></a>

```text
uart:~$ hfp ag outgoing 123456
AG outgoing call 0x20007690, number 123456
AG SCO connected 0x20005248
AG SCO info:
  SCO handle 0x0008
  SCO air mode 2
  SCO link type 2
uart:~$ hfp ag remote_ringing 0
AG call 0x20007690 start ringing mode 1
uart:~$ hfp ag remote_accept 0
AG call 0x20007690 accept
```

**HF 端的呼出时序（Outgoing Call Sequence on HF side）**

<a id="tab-0-T3V0Z29pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBIRiBzaWRl"></a>
<a id="panel-0-T3V0Z29pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBIRiBzaWRl"></a>

```text
uart:~$ hfp hf auto_select_codec enable
HF call 0x20007408 outgoing
codec negotiation: 1
codec auto selected: id 1
HF SCO connected 0x20005248
HF SCO info:
  SCO handle 0x0008
  SCO air mode 2
  SCO link type 2
HF remote call 0x20007408 start ringing
HF call 0x20007408 accepted
```

使用 HF 提供的电话号码发起呼叫：

**AG 端的呼出时序（Outgoing Call Sequence on AG side）**

<a id="tab-1-T3V0Z29pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBBRyBzaWRl"></a>
<a id="panel-1-T3V0Z29pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBBRyBzaWRl"></a>

```text
uart:~$
AG number call
AG outgoing call 0x20007690, number 123456789
AG SCO connected 0x20005248
AG SCO info:
  SCO handle 0x0008
  SCO air mode 2
  SCO link type 2
uart:~$ hfp ag remote_ringing 0
AG call 0x20007690 start ringing mode 1
uart:~$ hfp ag remote_accept 0
AG call 0x20007690 accept
```

**HF 端的呼出时序（Outgoing Call Sequence on HF side）**

<a id="tab-1-T3V0Z29pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBIRiBzaWRl"></a>
<a id="panel-1-T3V0Z29pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBIRiBzaWRl"></a>

```text
uart:~$ hfp hf auto_select_codec enable
uart:~$ hfp hf number_call 123456789
HF start dialing call: err 0
HF call 0x20007408 outgoing
codec negotiation: 1
codec auto selected: id 1
HF SCO connected 0x20005248
HF SCO info:
  SCO handle 0x0008
  SCO air mode 2
  SCO link type 2
HF remote call 0x20007408 start ringing
HF call 0x20007408 accepted
```

<a id="call-incoming"></a>

## 40.5 呼入电话（Call incoming）

从 AG 端接听来电：

**AG 端的呼入时序（Incoming Call Sequence on AG side）**

<a id="tab-2-SW5jb21pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBBRyBzaWRl"></a>
<a id="panel-2-SW5jb21pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBBRyBzaWRl"></a>

```text
uart:~$ hfp ag remote_incoming 123456
AG incoming call 0x20007690, number 123456
AG call 0x20007690 start ringing mode 1
AG SCO connected 0x20005248
AG SCO info:
  SCO handle 0x0008
  SCO air mode 2
  SCO link type 2
uart:~$ hfp ag accept 0
AG call 0x20007690 accept
```

**HF 端的呼入时序（Incoming Call Sequence on HF side）**

<a id="tab-2-SW5jb21pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBIRiBzaWRl"></a>
<a id="panel-2-SW5jb21pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBIRiBzaWRl"></a>

```text
uart:~$ hfp hf auto_select_codec enable
HF call 0x20007408 incoming
codec negotiation: 1
codec auto selected: id 1
HF SCO connected 0x20005248
HF SCO info:
  SCO handle 0x0008
  SCO air mode 2
  SCO link type 2
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 accepted
```

从 HF 端接听来电：

**AG 端的呼入时序（Incoming Call Sequence on AG side）**

<a id="tab-3-SW5jb21pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBBRyBzaWRl"></a>
<a id="panel-3-SW5jb21pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBBRyBzaWRl"></a>

```text
uart:~$ hfp ag remote_incoming 123456
AG incoming call 0x20007690, number 123456
AG codec negotiation result 0
AG call 0x20007690 start ringing mode 1
AG SCO connected 0x20005248
AG SCO info:
  SCO handle 0x0008
  SCO air mode 2
  SCO link type 2
AG call 0x20007690 accept
```

**HF 端的呼入时序（Incoming Call Sequence on HF side）**

<a id="tab-3-SW5jb21pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBIRiBzaWRl"></a>
<a id="panel-3-SW5jb21pbmcgQ2FsbCBTZXF1ZW5jZSBvbiBIRiBzaWRl"></a>

```text
uart:~$ hfp hf auto_select_codec enable
HF call 0x20007408 incoming
codec negotiation: 1
codec auto selected: id 1
HF SCO connected 0x20005248
HF SCO info:
  SCO handle 0x0008
  SCO air mode 2
  SCO link type 2
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
HF call 0x20007408 ring
HF call 0x20007408 CLIP 123456 0
uart:~$ hfp hf accept 0
HF call 0x20007408 accepted
```

<a id="call-termination"></a>

## 40.6 终止通话（Call termination）

呼出或呼入的电话接通后，音频网关（AG）或免提端（HF）任一方都可以终止通话。

从 AG 端终止通话：

**AG 端终止通话的时序（Call termination on AG side）**

<a id="tab-4-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBBRyBzaWRl"></a>
<a id="panel-4-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBBRyBzaWRl"></a>

```text
uart:~$ hfp ag terminate 0
AG call 0x20007690 terminate
AG SCO disconnected 0x20005248 (reason 22)
```

**HF 端终止通话的时序（Call termination on HF side）**

<a id="tab-4-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBIRiBzaWRl"></a>
<a id="panel-4-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBIRiBzaWRl"></a>

```text
HF call 0x20007408 terminated
HF SCO disconnected 0x20005248 (reason 22)
```

从 HF 端终止通话：

**AG 端终止通话的时序（Call termination on AG side）**

<a id="tab-5-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBBRyBzaWRl"></a>
<a id="panel-5-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBBRyBzaWRl"></a>

```text
AG call 0x20007690 terminate
AG SCO disconnected 0x20005248 (reason 22)
```

**HF 端终止通话的时序（Call termination on HF side）**

<a id="tab-5-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBIRiBzaWRl"></a>
<a id="panel-5-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBIRiBzaWRl"></a>

```text
uart:~$ hfp hf terminate 0
HF call 0x20007408 terminated
HF SCO disconnected 0x20005248 (reason 22)
```

从远端终止通话：

**AG 端终止通话的时序（Call termination on AG side）**

<a id="tab-6-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBBRyBzaWRl"></a>
<a id="panel-6-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBBRyBzaWRl"></a>

```text
uart:~$ hfp ag remote_terminate 0
AG call 0x20007690 terminate
AG SCO disconnected 0x20005248 (reason 22)
```

**HF 端终止通话的时序（Call termination on HF side）**

<a id="tab-6-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBIRiBzaWRl"></a>
<a id="panel-6-Q2FsbCB0ZXJtaW5hdGlvbiBvbiBIRiBzaWRl"></a>

```text
HF call 0x20007408 terminated
HF SCO disconnected 0x20005248 (reason 22)
```


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/classic/hfp.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/classic/hfp.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/classic/hfp.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：GOEP_Shell](P039_GOEP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：经典蓝牙L2CAP_Shell](P041_经典蓝牙L2CAP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P039_GOEP_Shell.md) · [返回大纲](大纲.md) · [下一章](P041_经典蓝牙L2CAP_Shell.md)

</details>

<!-- reading-navigation:end -->
