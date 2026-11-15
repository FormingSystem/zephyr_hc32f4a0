---
id: learning.zephyr-docs.shell-core-reference.page-3
title: Shell核心头文件源码
kind: reference
status: maintained
domains: [zephyr, shell, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell_2shell_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_Shell核心头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell_2shell_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P002_Shell核心头文件参考.md)和[公共接口](P001_Shell核心接口.md)；访问语义和生命周期见本页译注。

## 3.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00109"></a>
<a id="foldopen00120"></a>
<a id="foldopen00299"></a>
<a id="foldopen00317"></a>
<a id="foldopen00345"></a>
<a id="foldopen00383"></a>
<a id="foldopen00465"></a>
<a id="foldopen00481"></a>
<a id="foldopen00502"></a>
<a id="foldopen00531"></a>
<a id="foldopen00584"></a>
<a id="foldopen00599"></a>
<a id="foldopen00619"></a>
<a id="foldopen00641"></a>
<a id="foldopen00686"></a>
<a id="foldopen00701"></a>
<a id="foldopen00717"></a>
<a id="foldopen00773"></a>
<a id="foldopen00864"></a>
<a id="foldopen00949"></a>
<a id="foldopen01043"></a>
<a id="foldopen01121"></a>
<a id="foldopen01129"></a>
<a id="foldopen01204"></a>
<a id="foldopen01303"></a>
<a id="foldopen01480"></a>
<a id="aarch__interface_8h_html_a9fc2dce533bd7b8cb1fdd4bdbb2b62b1"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__log__api_html_ga224e4a75dca6d1b363ef49e96730dcfd"></a>
<a id="agroup__shell__api_html_ga05b2eb80f3484216ef2e1d4bf9492453"></a>
<a id="agroup__shell__api_html_ga061bf2530269ebf20d8e006dace5e33b"></a>
<a id="agroup__shell__api_html_ga07e76646c5065218464aa8ce78b75af3"></a>
<a id="agroup__shell__api_html_ga0844a0ce151551d3ccf45d507e5bab25"></a>
<a id="agroup__shell__api_html_ga0b6e69b499c153ae8f7ba256d445f09d"></a>
<a id="agroup__shell__api_html_ga182f247052041f1236d13726589885e2"></a>
<a id="agroup__shell__api_html_ga1fd1671311b112f0c87ab2dafd801105"></a>
<a id="agroup__shell__api_html_ga2113b7227b155755a7ab8a928f7ae499"></a>
<a id="agroup__shell__api_html_ga265807c2d8eba7b9ea633968627e085d"></a>
<a id="agroup__shell__api_html_ga2df2997c4b04f3246c22f43b274a353b"></a>
<a id="agroup__shell__api_html_ga313068db9c3b9972ca4129085d8605d5"></a>
<a id="agroup__shell__api_html_ga331e7d19b9b0755486596f5ffc598338"></a>
<a id="agroup__shell__api_html_ga4d51d4dbb22bed5d040deabc7ab6dc9d"></a>
<a id="agroup__shell__api_html_ga54dc053c92641bc9b9736bc2d61140f7"></a>
<a id="agroup__shell__api_html_ga56bf30741f9ec7a6d94e5c18c2858948"></a>
<a id="agroup__shell__api_html_ga571db3aa3e024a09e82b117a74d6f248"></a>
<a id="agroup__shell__api_html_ga6dcf569be711db32286fb1ef2dcf36d2"></a>
<a id="agroup__shell__api_html_ga706aebd24cbdb7f14b9a324515414ecf"></a>
<a id="agroup__shell__api_html_ga74a1c4edd803cad14c893fc9816e534f"></a>
<a id="agroup__shell__api_html_ga768c606f2d50f24e9b607ba0a341686d"></a>
<a id="agroup__shell__api_html_ga79369ddfea2dc2cb5813c5eb5c67634a"></a>
<a id="agroup__shell__api_html_ga7d5873456ba43ebd3cc86d25e3f4a72c"></a>
<a id="agroup__shell__api_html_ga7e66389d0faf15a2a7c31c68cdd9c36c"></a>
<a id="agroup__shell__api_html_ga7fb40045dc0a27c175e37a6c9cd84b53"></a>
<a id="agroup__shell__api_html_ga80ff4b3b4cc62e543fd510c14f55b42a"></a>
<a id="agroup__shell__api_html_ga86fade2757d04c9220d5912a4ee540a0"></a>
<a id="agroup__shell__api_html_ga8764ff11603855a10419c48e46e8221c"></a>
<a id="agroup__shell__api_html_ga8e83709f5e75d4cea51f42f41bb4e20f"></a>
<a id="agroup__shell__api_html_ga919147e222fe10ce14ab3c3a5c5a94e3"></a>
<a id="agroup__shell__api_html_ga9e4911ff2c3a07fa70711ddac83701d6"></a>
<a id="agroup__shell__api_html_ga9f2994f2d6a55521a3e162a81299e4c3"></a>
<a id="agroup__shell__api_html_gaa2b8cf8ac78b8355408ef94958ebdc70"></a>
<a id="agroup__shell__api_html_gabfb6a1f1f53f90365de349348015311e"></a>
<a id="agroup__shell__api_html_gacaddbcd6e84f377f39a5d69398996557"></a>
<a id="agroup__shell__api_html_gad27754d0beb31bc501f28f9ef26a362c"></a>
<a id="agroup__shell__api_html_gad386d4e8077103e7976f25996fcc3132"></a>
<a id="agroup__shell__api_html_gad53881371bbaedfd3ef3ecf219706fd1"></a>
<a id="agroup__shell__api_html_gae2a8e3d44a9bf5eb55be80833ac6eb5d"></a>
<a id="agroup__shell__api_html_gaeeba0b483974205c54e364d509badd42"></a>
<a id="agroup__shell__api_html_gaf1f41d8b6cd430357d593ab0fc5adfeb"></a>
<a id="agroup__shell__api_html_gafc042f32bac2fdd4cbde9f943e29b008"></a>
<a id="agroup__shell__api_html_gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab"></a>
<a id="agroup__shell__api_html_gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="akernel_2thread_8h_html_a6379f5a1f19ffbc262a6877c4f6e3647"></a>
<a id="akernel_8h_html"></a>
<a id="alog_8h_html"></a>
<a id="alog__instance_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="ashell__fprintf_8h_html"></a>
<a id="ashell__history_8h_html"></a>
<a id="ashell__log__backend_8h_html"></a>
<a id="ashell__remote__cli_8h_html"></a>
<a id="ashell__string__conv_8h_html"></a>
<a id="ashell__types_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a1e74e8d3b0b1a981c67e1d0284ccac3d"></a>
<a id="astructk__event_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__thread_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructlog__backend__api_html"></a>
<a id="astructlog__backend_html"></a>
<a id="astructshell__cmd__help_html"></a>
<a id="astructshell__cmd__help_html_a3735f4afeeea3d968d9e8fc74e0aa68f"></a>
<a id="astructshell__cmd__help_html_af9e182e1599c3cfcc42f739d40a511bb"></a>
<a id="astructshell__ctx_html"></a>
<a id="astructshell__static__args_html"></a>
<a id="astructshell__static__args_html_a21f53604a733e4351687a71d45909abd"></a>
<a id="astructshell__static__args_html_a2b3bab087c7f7bed6217df86d6577925"></a>
<a id="astructshell__static__args_html_a2c23bfa755d3bb651e299ff461065d98"></a>
<a id="astructshell__static__args_html_aa3aa836ed537dde38e64d2c677ace5ae"></a>
<a id="astructshell__static__entry_html"></a>
<a id="astructshell__static__entry_html_a14534428d81f5ffeb303a5320766cd0a"></a>
<a id="astructshell__static__entry_html_a3147eb0cc1fea698dd433127acb1f220"></a>
<a id="astructshell__static__entry_html_a73951d31712342c0c0545a142059d367"></a>
<a id="astructshell__static__entry_html_ac8fb0fc23957a49d9a3664b5baa08704"></a>
<a id="astructshell__static__entry_html_ad87defa749ee7481f6d29d8c9084fb91"></a>
<a id="astructshell__transport__api_html"></a>
<a id="astructshell__transport__api_html_a3b447d16d7c30f994c582d67bde57ba8"></a>
<a id="astructshell__transport__api_html_a59afba962312a077343b440448d67135"></a>
<a id="astructshell__transport__api_html_a6bbf2905abcbf6ca564ecf3f07d95712"></a>
<a id="astructshell__transport__api_html_a94cc7843174a4aba668389a4b46928d3"></a>
<a id="astructshell__transport__api_html_a95535c7195088e68230ecb306f105713"></a>
<a id="astructshell__transport__api_html_aae0e8ad92065dbff10691c28045d0c8f"></a>
<a id="astructshell__transport_html"></a>
<a id="astructshell__transport_html_a02f44bb376152452f5b5d20f33ccbdf6"></a>
<a id="astructshell__transport_html_ab4bee270415b445ded5a8ba6e8cb3a25"></a>
<a id="astructshell_html"></a>
<a id="astructsys__getopt__state_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="asys__getopt_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="aunionshell__cmd__entry_html"></a>
<a id="aunionshell__cmd__entry_html_a4abb8327df0e62f63432a05cc885f03d"></a>
<a id="aunionshell__cmd__entry_html_aa76e35866f5df37593705fd1b53e15df"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00017"></a>#include &lt;zephyr/shell/shell_types.h&gt;
<a id="l00018"></a>#include &lt;zephyr/shell/shell_history.h&gt;
<a id="l00019"></a>#include &lt;zephyr/shell/shell_fprintf.h&gt;
<a id="l00020"></a>#include &lt;zephyr/shell/shell_log_backend.h&gt;
<a id="l00021"></a>#include &lt;zephyr/shell/shell_string_conv.h&gt;
<a id="l00022"></a>#include &lt;zephyr/logging/log_instance.h&gt;
<a id="l00023"></a>#include &lt;zephyr/logging/log.h&gt;
<a id="l00024"></a>#include &lt;zephyr/sys/iterable_sections.h&gt;
<a id="l00025"></a>#include &lt;zephyr/sys/util.h&gt;
<a id="l00026"></a>#include &lt;zephyr/toolchain.h&gt;
<a id="l00027"></a>
<a id="l00028"></a>#if defined CONFIG_SHELL_GETOPT
<a id="l00029"></a>#include &lt;zephyr/sys/sys_getopt.h&gt;
<a id="l00030"></a>#endif
<a id="l00031"></a>
<a id="l00032"></a>#ifdef __cplusplus
<a id="l00033"></a>extern "C" {
<a id="l00034"></a>#endif
<a id="l00035"></a>
<a id="l00037"></a>#ifndef CONFIG_SHELL_PROMPT_BUFF_SIZE
<a id="l00038"></a>#define CONFIG_SHELL_PROMPT_BUFF_SIZE 0
<a id="l00039"></a>#endif
<a id="l00040"></a>
<a id="l00041"></a>#ifndef CONFIG_SHELL_CMD_BUFF_SIZE
<a id="l00042"></a>#define CONFIG_SHELL_CMD_BUFF_SIZE 0
<a id="l00043"></a>#endif
<a id="l00044"></a>
<a id="l00045"></a>#ifndef CONFIG_SHELL_PRINTF_BUFF_SIZE
<a id="l00046"></a>#define CONFIG_SHELL_PRINTF_BUFF_SIZE 0
<a id="l00047"></a>#endif
<a id="l00048"></a>
<a id="l00049"></a>#ifndef CONFIG_SHELL_HISTORY_BUFFER
<a id="l00050"></a>#define CONFIG_SHELL_HISTORY_BUFFER 0
<a id="l00051"></a>#endif
<a id="l00052"></a>
<a id="l00053"></a>#define Z_SHELL_CMD_ROOT_LVL            (0u)
<a id="l00054"></a>
<a id="l00055"></a>#define SHELL_HEXDUMP_BYTES_IN_LINE     16
<a id="l00057"></a>
<a id="l00065"></a>
<a id="l00077"></a>#define SHELL_OPT_ARG_RAW       (0xFE)
<a id="l00078"></a>
<a id="l00082"></a>#define SHELL_OPT_ARG_CHECK_SKIP (0xFF)
<a id="l00083"></a>
<a id="l00088"></a>#define SHELL_OPT_ARG_MAX               (0xFD)
<a id="l00089"></a>
<a id="l00090"></a>struct shell_static_entry;
<a id="l00091"></a>
<a id="l00103"></a>typedef void (*shell_dynamic_get)(size_t idx,
<a id="l00104"></a>                                  struct shell_static_entry *entry);
<a id="l00105"></a>
<a id="l00109"></a>union shell_cmd_entry {
<a id="l00111"></a>        shell_dynamic_get dynamic_get;
<a id="l00112"></a>
<a id="l00114"></a>        const struct shell_static_entry *entry;
<a id="l00115"></a>};
<a id="l00116"></a>
<a id="l00117"></a>struct shell;
<a id="l00118"></a>
<a id="l00120"></a>struct shell_static_args {
<a id="l00121"></a>        uint8_t mandatory;
<a id="l00122"></a>        uint8_t optional;
<a id="l00123"></a>        uint16_t remote_cmd: 2;
<a id="l00124"></a>        uint16_t remote_id: 4;
<a id="l00125"></a>};
<a id="l00126"></a>
<a id="l00128"></a>#define SHELL_CMD_FLAG_REMOTE_ROOT BIT(0)
<a id="l00129"></a>
<a id="l00131"></a>#define SHELL_CMD_FLAG_REMOTE_SUBCMD BIT(1)
<a id="l00132"></a>
<a id="l00148"></a>const struct device *shell_device_lookup(size_t idx,
<a id="l00149"></a>                                         const char *prefix);
<a id="l00150"></a>
<a id="l00167"></a>const struct device *shell_device_lookup_all(size_t idx,
<a id="l00168"></a>                                             const char *prefix);
<a id="l00169"></a>
<a id="l00185"></a>const struct device *shell_device_lookup_non_ready(size_t idx,
<a id="l00186"></a>                                                   const char *prefix);
<a id="l00187"></a>
<a id="l00198"></a>typedef bool (*shell_device_filter_t)(const struct device *dev);
<a id="l00199"></a>
<a id="l00213"></a>const struct device *shell_device_filter(size_t idx,
<a id="l00214"></a>                                         shell_device_filter_t filter);
<a id="l00215"></a>
<a id="l00236"></a>const struct device *shell_device_get_binding(const char *name);
<a id="l00237"></a>
<a id="l00253"></a>const struct device *shell_device_get_binding_all(const char *name);
<a id="l00254"></a>
<a id="l00267"></a>typedef int (*shell_cmd_handler)(const struct shell *sh,
<a id="l00268"></a>                                 size_t argc, char **argv);
<a id="l00269"></a>
<a id="l00283"></a>typedef int (*shell_dict_cmd_handler)(const struct shell *sh, size_t argc,
<a id="l00284"></a>                                      char **argv, void *data);
<a id="l00285"></a>
<a id="l00286"></a>/* When entries are added to the memory section a padding is applied for
<a id="l00287"></a> * the posix architecture with 64bits builds and x86_64 targets. Adding padding to allow handle data
<a id="l00288"></a> * in the memory section as array.
<a id="l00289"></a> */
<a id="l00290"></a>#if (defined(CONFIG_ARCH_POSIX) &amp;&amp; defined(CONFIG_64BIT)) || defined(CONFIG_X86_64)
<a id="l00291"></a>#define Z_SHELL_STATIC_ENTRY_PADDING 24
<a id="l00292"></a>#else
<a id="l00293"></a>#define Z_SHELL_STATIC_ENTRY_PADDING 0
<a id="l00294"></a>#endif
<a id="l00295"></a>
<a id="l00299"></a>struct shell_static_entry {
<a id="l00300"></a>        const char *syntax;
<a id="l00301"></a>        const char *help;
<a id="l00302"></a>        const union shell_cmd_entry *subcmd;
<a id="l00303"></a>        shell_cmd_handler handler;
<a id="l00304"></a>        struct shell_static_args args;
<a id="l00306"></a>        uint8_t padding[Z_SHELL_STATIC_ENTRY_PADDING];
<a id="l00308"></a>};
<a id="l00309"></a>
<a id="l00317"></a>struct shell_cmd_help {
<a id="l00319"></a>        uint32_t magic;
<a id="l00321"></a>        const char *description;
<a id="l00322"></a>        const char *usage;
<a id="l00323"></a>};
<a id="l00324"></a>
<a id="l00328"></a>
<a id="l00333"></a>#define SHELL_STRUCTURED_HELP_MAGIC 0x86D20BC4U
<a id="l00334"></a>
<a id="l00338"></a>
<a id="l00345"></a>static inline bool shell_help_is_structured(const char *help)
<a id="l00346"></a>{
<a id="l00347"></a>        const uint32_t magic32 = SHELL_STRUCTURED_HELP_MAGIC;
<a id="l00348"></a>        const char *magic = (const char *)&amp;magic32;
<a id="l00349"></a>
<a id="l00355"></a>        return help != NULL &amp;&amp; (magic[0] == help[0]) &amp;&amp; (magic[1] == help[1])
<a id="l00356"></a>               &amp;&amp; (magic[2] == help[2]) &amp;&amp; (magic[3] == help[3]);
<a id="l00357"></a>}
<a id="l00358"></a>
<a id="l00359"></a>#if defined(CONFIG_SHELL_HELP) || defined(__DOXYGEN__)
<a id="l00383"></a>#define SHELL_HELP(_description, _usage)                                                           \
<a id="l00384"></a>        ((const char *)&amp;(const struct shell_cmd_help){                                             \
<a id="l00385"></a>                .magic = SHELL_STRUCTURED_HELP_MAGIC,                                              \
<a id="l00386"></a>                .description = (_description),                                                     \
<a id="l00387"></a>                .usage = (_usage),                                                                 \
<a id="l00388"></a>        })
<a id="l00389"></a>#else
<a id="l00390"></a>#define SHELL_HELP(_description, _usage) NULL
<a id="l00391"></a>#endif /* CONFIG_SHELL_HELP */
<a id="l00392"></a>
<a id="l00408"></a>#define SHELL_CMD_ARG_REGISTER(syntax, subcmd, help, handler,              \
<a id="l00409"></a>                               mandatory, optional)                        \
<a id="l00410"></a>        static const struct shell_static_entry UTIL_CAT(_shell_, syntax) = \
<a id="l00411"></a>        SHELL_CMD_ARG(syntax, subcmd, help, handler, mandatory, optional); \
<a id="l00412"></a>        static const TYPE_SECTION_ITERABLE(union shell_cmd_entry,          \
<a id="l00413"></a>                UTIL_CAT(shell_cmd_, syntax), shell_root_cmds,             \
<a id="l00414"></a>                UTIL_CAT(shell_cmd_, syntax)                               \
<a id="l00415"></a>        ) = {                                                              \
<a id="l00416"></a>                .entry = &amp;UTIL_CAT(_shell_, syntax)                        \
<a id="l00417"></a>        }
<a id="l00418"></a>
<a id="l00439"></a>#define SHELL_COND_CMD_ARG_REGISTER(flag, syntax, subcmd, help, handler, \
<a id="l00440"></a>                                        mandatory, optional) \
<a id="l00441"></a>        COND_CODE_1(\
<a id="l00442"></a>                flag, \
<a id="l00443"></a>                (\
<a id="l00444"></a>                SHELL_CMD_ARG_REGISTER(syntax, subcmd, help, handler, \
<a id="l00445"></a>                                        mandatory, optional) \
<a id="l00446"></a>                ), \
<a id="l00447"></a>                (\
<a id="l00448"></a>                static shell_cmd_handler dummy_##syntax##_handler __unused = \
<a id="l00449"></a>                                                                handler;\
<a id="l00450"></a>                static const union shell_cmd_entry *dummy_subcmd_##syntax \
<a id="l00451"></a>                        __unused = subcmd\
<a id="l00452"></a>                ) \
<a id="l00453"></a>        )
<a id="l00465"></a>#define SHELL_CMD_REGISTER(syntax, subcmd, help, handler) \
<a id="l00466"></a>        SHELL_CMD_ARG_REGISTER(syntax, subcmd, help, handler, 0, 0)
<a id="l00467"></a>
<a id="l00481"></a>#define SHELL_COND_CMD_REGISTER(flag, syntax, subcmd, help, handler) \
<a id="l00482"></a>        SHELL_COND_CMD_ARG_REGISTER(flag, syntax, subcmd, help, handler, 0, 0)
<a id="l00483"></a>
<a id="l00502"></a>#define SHELL_STATIC_SUBCMD_SET_CREATE(name, ...)                       \
<a id="l00503"></a>        static const struct shell_static_entry shell_##name[] = {       \
<a id="l00504"></a>                __VA_ARGS__                                             \
<a id="l00505"></a>        };                                                              \
<a id="l00506"></a>        static const union shell_cmd_entry name = {                     \
<a id="l00507"></a>                .entry = shell_##name                                   \
<a id="l00508"></a>        }
<a id="l00509"></a>
<a id="l00510"></a>#define Z_SHELL_UNDERSCORE(x) _##x
<a id="l00511"></a>#define Z_SHELL_SUBCMD_NAME(...) \
<a id="l00512"></a>        UTIL_CAT(shell_subcmds, MACRO_MAP_CAT(Z_SHELL_UNDERSCORE, __VA_ARGS__))
<a id="l00513"></a>#define Z_SHELL_SUBCMD_SECTION_TAG(...) MACRO_MAP_CAT(Z_SHELL_UNDERSCORE, __VA_ARGS__)
<a id="l00514"></a>#define Z_SHELL_SUBCMD_SET_SECTION_TAG(x) \
<a id="l00515"></a>        Z_SHELL_SUBCMD_SECTION_TAG(NUM_VA_ARGS_LESS_1 x, __DEBRACKET x)
<a id="l00516"></a>#define Z_SHELL_SUBCMD_ADD_SECTION_TAG(x, y) \
<a id="l00517"></a>        Z_SHELL_SUBCMD_SECTION_TAG(NUM_VA_ARGS_LESS_1 x, __DEBRACKET x, y)
<a id="l00518"></a>
<a id="l00530"></a>
<a id="l00531"></a>#define SHELL_SUBCMD_SET_CREATE(_name, _parent) \
<a id="l00532"></a>        static const TYPE_SECTION_ITERABLE(struct shell_static_entry, _name, shell_subcmds, \
<a id="l00533"></a>                                          Z_SHELL_SUBCMD_SET_SECTION_TAG(_parent))
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00555"></a>#define SHELL_SUBCMD_COND_ADD(_flag, _parent, _syntax, _subcmd, _help, _handler, \
<a id="l00556"></a>                           _mand, _opt) \
<a id="l00557"></a>        COND_CODE_1(_flag, \
<a id="l00558"></a>                (static const TYPE_SECTION_ITERABLE(struct shell_static_entry, \
<a id="l00559"></a>                                        Z_SHELL_SUBCMD_NAME(__DEBRACKET _parent, _syntax), \
<a id="l00560"></a>                                        shell_subcmds, \
<a id="l00561"></a>                                        Z_SHELL_SUBCMD_ADD_SECTION_TAG(_parent, _syntax)) = \
<a id="l00562"></a>                        SHELL_EXPR_CMD_ARG(1, _syntax, _subcmd, _help, \
<a id="l00563"></a>                                           _handler, _mand, _opt, 0, 0)\
<a id="l00564"></a>                ), \
<a id="l00565"></a>                (static shell_cmd_handler dummy_handler_##_syntax __unused = _handler;\
<a id="l00566"></a>                 static const union shell_cmd_entry dummy_subcmd_##_syntax __unused = { \
<a id="l00567"></a>                        .entry = (const struct shell_static_entry *)_subcmd\
<a id="l00568"></a>                 } \
<a id="l00569"></a>                ) \
<a id="l00570"></a>        )
<a id="l00571"></a>
<a id="l00584"></a>#define SHELL_SUBCMD_ADD(_parent, _syntax, _subcmd, _help, _handler, _mand, _opt) \
<a id="l00585"></a>        SHELL_SUBCMD_COND_ADD(1, _parent, _syntax, _subcmd, _help, _handler, _mand, _opt)
<a id="l00586"></a>
<a id="l00591"></a>#define SHELL_SUBCMD_SET_END {0}
<a id="l00592"></a>
<a id="l00599"></a>#define SHELL_DYNAMIC_CMD_CREATE(name, get)                                     \
<a id="l00600"></a>        static const TYPE_SECTION_ITERABLE(union shell_cmd_entry, name,         \
<a id="l00601"></a>                shell_dynamic_subcmds, name) =                                  \
<a id="l00602"></a>        {                                                                       \
<a id="l00603"></a>                .dynamic_get = get                                              \
<a id="l00604"></a>        }
<a id="l00605"></a>
<a id="l00619"></a>#define SHELL_CMD_ARG(syntax, subcmd, help, handler, mand, opt) \
<a id="l00620"></a>        SHELL_EXPR_CMD_ARG(1, syntax, subcmd, help, handler, mand, opt, 0, 0)
<a id="l00621"></a>
<a id="l00641"></a>#define SHELL_COND_CMD_ARG(flag, syntax, subcmd, help, handler, mand, opt) \
<a id="l00642"></a>        SHELL_EXPR_CMD_ARG(IS_ENABLED(flag), syntax, subcmd, help, \
<a id="l00643"></a>                          handler, mand, opt, 0, 0)
<a id="l00644"></a>
<a id="l00666"></a>#define SHELL_EXPR_CMD_ARG(_expr, _syntax, _subcmd, _help, _handler, \
<a id="l00667"></a>                           _mand, _opt, _remote_cmd, _remote_id) \
<a id="l00668"></a>        { \
<a id="l00669"></a>                .syntax = (_expr) ? (const char *)STRINGIFY(_syntax) : "", \
<a id="l00670"></a>                .help  = (_expr) ? (const char *)_help : NULL, \
<a id="l00671"></a>                .subcmd = (const union shell_cmd_entry *)((_expr) ? \
<a id="l00672"></a>                                _subcmd : NULL), \
<a id="l00673"></a>                .handler = (shell_cmd_handler)((_expr) ? _handler : NULL), \
<a id="l00674"></a>                .args = { .mandatory = _mand, .optional = _opt, \
<a id="l00675"></a>                        .remote_cmd = _remote_cmd, .remote_id = _remote_id } \
<a id="l00676"></a>        }
<a id="l00677"></a>
<a id="l00686"></a>#define SHELL_CMD(_syntax, _subcmd, _help, _handler) \
<a id="l00687"></a>        SHELL_CMD_ARG(_syntax, _subcmd, _help, _handler, 0, 0)
<a id="l00688"></a>
<a id="l00701"></a>#define SHELL_COND_CMD(_flag, _syntax, _subcmd, _help, _handler) \
<a id="l00702"></a>        SHELL_COND_CMD_ARG(_flag, _syntax, _subcmd, _help, _handler, 0, 0)
<a id="l00703"></a>
<a id="l00717"></a>#define SHELL_EXPR_CMD(_expr, _syntax, _subcmd, _help, _handler) \
<a id="l00718"></a>        SHELL_EXPR_CMD_ARG(_expr, _syntax, _subcmd, _help, _handler, 0, 0, 0, 0)
<a id="l00719"></a>
<a id="l00721"></a>
<a id="l00722"></a>/* Internal macro used for creating handlers for dictionary commands. */
<a id="l00723"></a>#define Z_SHELL_CMD_DICT_HANDLER_CREATE(_data, _handler)                \
<a id="l00724"></a>static int UTIL_CAT(UTIL_CAT(cmd_dict_, UTIL_CAT(_handler, _)),         \
<a id="l00725"></a>                        GET_ARG_N(1, __DEBRACKET _data))(               \
<a id="l00726"></a>                const struct shell *sh, size_t argc, char **argv)       \
<a id="l00727"></a>{                                                                       \
<a id="l00728"></a>        return _handler(sh, argc, argv,                                 \
<a id="l00729"></a>                        (void *)GET_ARG_N(2, __DEBRACKET _data));       \
<a id="l00730"></a>}
<a id="l00731"></a>
<a id="l00732"></a>/* Internal macro used for creating dictionary commands. */
<a id="l00733"></a>#define SHELL_CMD_DICT_CREATE(_data, _handler)                          \
<a id="l00734"></a>        SHELL_CMD_ARG(GET_ARG_N(1, __DEBRACKET _data), NULL, GET_ARG_N(3, __DEBRACKET _data),   \
<a id="l00735"></a>                UTIL_CAT(UTIL_CAT(cmd_dict_, UTIL_CAT(_handler, _)),    \
<a id="l00736"></a>                        GET_ARG_N(1, __DEBRACKET _data)), 1, 0)
<a id="l00737"></a>
<a id="l00739"></a>
<a id="l00773"></a>#define SHELL_SUBCMD_DICT_SET_CREATE(_name, _handler, ...)              \
<a id="l00774"></a>        FOR_EACH_FIXED_ARG(Z_SHELL_CMD_DICT_HANDLER_CREATE, (),         \
<a id="l00775"></a>                           _handler, __VA_ARGS__)                       \
<a id="l00776"></a>        SHELL_STATIC_SUBCMD_SET_CREATE(_name,                           \
<a id="l00777"></a>                FOR_EACH_FIXED_ARG(SHELL_CMD_DICT_CREATE, (,), _handler, __VA_ARGS__),  \
<a id="l00778"></a>                SHELL_SUBCMD_SET_END                                    \
<a id="l00779"></a>        )
<a id="l00780"></a>
<a id="l00782"></a>
<a id="l00787"></a>enum shell_receive_state {
<a id="l00788"></a>        SHELL_RECEIVE_DEFAULT,
<a id="l00789"></a>        SHELL_RECEIVE_ESC,
<a id="l00790"></a>        SHELL_RECEIVE_ESC_SEQ,
<a id="l00791"></a>        SHELL_RECEIVE_TILDE_EXP
<a id="l00792"></a>};
<a id="l00793"></a>
<a id="l00797"></a>enum shell_state {
<a id="l00798"></a>        SHELL_STATE_UNINITIALIZED,
<a id="l00799"></a>        SHELL_STATE_INITIALIZED,
<a id="l00800"></a>        SHELL_STATE_ACTIVE,
<a id="l00801"></a>        SHELL_STATE_PANIC_MODE_ACTIVE,
<a id="l00802"></a>        SHELL_STATE_PANIC_MODE_INACTIVE
<a id="l00803"></a>};
<a id="l00804"></a>
<a id="l00806"></a>enum shell_transport_evt {
<a id="l00807"></a>        SHELL_TRANSPORT_EVT_RX_RDY,
<a id="l00808"></a>        SHELL_TRANSPORT_EVT_TX_RDY
<a id="l00809"></a>};
<a id="l00810"></a>
<a id="l00811"></a>enum shell_readline_state {
<a id="l00812"></a>        SHELL_READLINE_INACTIVE,
<a id="l00813"></a>        SHELL_READLINE_ACTIVE,
<a id="l00814"></a>        SHELL_READLINE_DONE,
<a id="l00815"></a>        SHELL_READLINE_CANCELED,
<a id="l00816"></a>};
<a id="l00817"></a>
<a id="l00819"></a>
<a id="l00831"></a>typedef void (*shell_transport_handler_t)(enum shell_transport_evt evt,
<a id="l00832"></a>                                          void *context);
<a id="l00833"></a>
<a id="l00844"></a>typedef void (*shell_uninit_cb_t)(const struct shell *sh, int res);
<a id="l00845"></a>
<a id="l00853"></a>typedef void (*shell_bypass_cb_t)(const struct shell *sh,
<a id="l00854"></a>                                  uint8_t *data,
<a id="l00855"></a>                                  size_t len,
<a id="l00856"></a>                                  void *user_data);
<a id="l00857"></a>
<a id="l00858"></a>struct shell_transport;
<a id="l00859"></a>
<a id="l00864"></a>struct shell_transport_api {
<a id="l00876"></a>        int (*init)(const struct shell_transport *transport,
<a id="l00877"></a>                    const void *config,
<a id="l00878"></a>                    shell_transport_handler_t evt_handler,
<a id="l00879"></a>                    void *context);
<a id="l00880"></a>
<a id="l00888"></a>        int (*uninit)(const struct shell_transport *transport);
<a id="l00889"></a>
<a id="l00902"></a>        int (*enable)(const struct shell_transport *transport,
<a id="l00903"></a>                      bool blocking_tx);
<a id="l00904"></a>
<a id="l00915"></a>        int (*write)(const struct shell_transport *transport,
<a id="l00916"></a>                     const void *data, size_t length, size_t *cnt);
<a id="l00917"></a>
<a id="l00928"></a>        int (*read)(const struct shell_transport *transport,
<a id="l00929"></a>                    void *data, size_t length, size_t *cnt);
<a id="l00930"></a>
<a id="l00938"></a>        void (*update)(const struct shell_transport *transport);
<a id="l00939"></a>
<a id="l00940"></a>};
<a id="l00941"></a>
<a id="l00949"></a>struct shell_transport {
<a id="l00950"></a>        const struct shell_transport_api *api;
<a id="l00951"></a>        void *ctx;
<a id="l00952"></a>};
<a id="l00953"></a>
<a id="l00955"></a>
<a id="l00959"></a>struct shell_stats {
<a id="l00960"></a>        atomic_t log_lost_cnt;
<a id="l00961"></a>};
<a id="l00962"></a>
<a id="l00963"></a>#ifdef CONFIG_SHELL_STATS
<a id="l00964"></a>#define Z_SHELL_STATS_DEFINE(_name) static struct shell_stats _name##_stats
<a id="l00965"></a>#define Z_SHELL_STATS_PTR(_name) (&amp;(_name##_stats))
<a id="l00966"></a>#else
<a id="l00967"></a>#define Z_SHELL_STATS_DEFINE(_name)
<a id="l00968"></a>#define Z_SHELL_STATS_PTR(_name) NULL
<a id="l00969"></a>#endif /* CONFIG_SHELL_STATS */
<a id="l00970"></a>
<a id="l00974"></a>struct shell_backend_config_flags {
<a id="l00975"></a>        uint32_t insert_mode :1;
<a id="l00976"></a>        uint32_t echo        :1;
<a id="l00977"></a>        uint32_t obscure     :1;
<a id="l00978"></a>        uint32_t mode_delete :1;
<a id="l00979"></a>        uint32_t use_colors  :1;
<a id="l00980"></a>        uint32_t use_vt100   :1;
<a id="l00981"></a>        uint32_t _reserved   :26;
<a id="l00982"></a>};
<a id="l00983"></a>
<a id="l00984"></a>BUILD_ASSERT((sizeof(struct shell_backend_config_flags) == sizeof(uint32_t)),
<a id="l00985"></a>             "Structure must fit in 4 bytes");
<a id="l00986"></a>
<a id="l00990"></a>#define SHELL_DEFAULT_BACKEND_CONFIG_FLAGS                              \
<a id="l00991"></a>{                                                                       \
<a id="l00992"></a>        .insert_mode    = 0,                                            \
<a id="l00993"></a>        .echo           = 1,                                            \
<a id="l00994"></a>        .obscure        = IS_ENABLED(CONFIG_SHELL_START_OBSCURED),      \
<a id="l00995"></a>        .mode_delete    = 1,                                            \
<a id="l00996"></a>        .use_colors     = 1,                                            \
<a id="l00997"></a>        .use_vt100      = 1,                                            \
<a id="l00998"></a>};
<a id="l00999"></a>
<a id="l01000"></a>struct shell_backend_ctx_flags {
<a id="l01001"></a>        uint32_t last_nl      :8;
<a id="l01002"></a>        uint32_t processing   :1;
<a id="l01003"></a>        uint32_t tx_rdy       :1;
<a id="l01004"></a>        uint32_t history_exit :1;
<a id="l01005"></a>        uint32_t cmd_ctx      :1;
<a id="l01006"></a>        uint32_t print_noinit :1;
<a id="l01007"></a>        uint32_t sync_mode    :1;
<a id="l01008"></a>        uint32_t handle_log   :1;
<a id="l01009"></a>        uint32_t _reserved    :17;
<a id="l01010"></a>};
<a id="l01011"></a>
<a id="l01012"></a>BUILD_ASSERT((sizeof(struct shell_backend_ctx_flags) == sizeof(uint32_t)),
<a id="l01013"></a>             "Structure must fit in 4 bytes");
<a id="l01014"></a>
<a id="l01018"></a>union shell_backend_cfg {
<a id="l01019"></a>        atomic_t value;
<a id="l01020"></a>        struct shell_backend_config_flags flags;
<a id="l01021"></a>};
<a id="l01022"></a>
<a id="l01026"></a>union shell_backend_ctx {
<a id="l01027"></a>        uint32_t value;
<a id="l01028"></a>        struct shell_backend_ctx_flags flags;
<a id="l01029"></a>};
<a id="l01030"></a>
<a id="l01031"></a>enum shell_signal {
<a id="l01032"></a>        SHELL_SIGNAL_RXRDY = BIT(0),
<a id="l01033"></a>        SHELL_SIGNAL_LOG_MSG = BIT(1),
<a id="l01034"></a>        SHELL_SIGNAL_KILL = BIT(2),
<a id="l01035"></a>        SHELL_SIGNAL_TXDONE = BIT(3),
<a id="l01036"></a>};
<a id="l01037"></a>
<a id="l01039"></a>
<a id="l01043"></a>struct shell_ctx {
<a id="l01045"></a>#if defined(CONFIG_SHELL_PROMPT_CHANGE) &amp;&amp; CONFIG_SHELL_PROMPT_CHANGE
<a id="l01046"></a>        char prompt[CONFIG_SHELL_PROMPT_BUFF_SIZE];
<a id="l01047"></a>#else
<a id="l01048"></a>        const char *prompt;
<a id="l01049"></a>#endif
<a id="l01050"></a>
<a id="l01051"></a>        enum shell_state state;
<a id="l01052"></a>        enum shell_receive_state receive_state;
<a id="l01053"></a>
<a id="l01055"></a>        enum shell_readline_state readline_state;
<a id="l01056"></a>
<a id="l01058"></a>        const char *readline_prompt;
<a id="l01059"></a>
<a id="l01061"></a>        struct shell_static_entry active_cmd;
<a id="l01062"></a>
<a id="l01064"></a>        const struct shell_static_entry *selected_cmd;
<a id="l01065"></a>
<a id="l01067"></a>        struct shell_vt100_ctx vt100_ctx;
<a id="l01068"></a>
<a id="l01072"></a>        shell_uninit_cb_t uninit_cb;
<a id="l01073"></a>
<a id="l01075"></a>        shell_bypass_cb_t bypass;
<a id="l01076"></a>
<a id="l01078"></a>        void *bypass_user_data;
<a id="l01079"></a>
<a id="l01081"></a>        uint32_t log_level;
<a id="l01082"></a>
<a id="l01083"></a>#if defined CONFIG_SHELL_GETOPT
<a id="l01085"></a>        struct sys_getopt_state getopt;
<a id="l01086"></a>#endif
<a id="l01087"></a>
<a id="l01088"></a>        uint16_t cmd_buff_len;
<a id="l01089"></a>        uint16_t cmd_buff_pos;
<a id="l01090"></a>
<a id="l01091"></a>        uint16_t cmd_tmp_buff_len;
<a id="l01092"></a>        uint16_t cmd_tmp_buff_pos;
<a id="l01093"></a>
<a id="l01095"></a>        char cmd_buff[CONFIG_SHELL_CMD_BUFF_SIZE];
<a id="l01096"></a>
<a id="l01098"></a>        char temp_buff[CONFIG_SHELL_CMD_BUFF_SIZE];
<a id="l01099"></a>
<a id="l01101"></a>        char printf_buff[CONFIG_SHELL_PRINTF_BUFF_SIZE];
<a id="l01102"></a>
<a id="l01103"></a>        volatile union shell_backend_cfg cfg;
<a id="l01104"></a>        volatile union shell_backend_ctx ctx;
<a id="l01105"></a>
<a id="l01106"></a>        struct k_event signal_event;
<a id="l01107"></a>
<a id="l01108"></a>        struct k_sem lock_sem;
<a id="l01109"></a>        k_tid_t tid;
<a id="l01110"></a>        int ret_val;
<a id="l01112"></a>};
<a id="l01113"></a>
<a id="l01115"></a>extern const struct log_backend_api log_backend_shell_api;
<a id="l01117"></a>
<a id="l01121"></a>enum shell_flag {
<a id="l01122"></a>        SHELL_FLAG_CRLF_DEFAULT = (1&lt;&lt;0),
<a id="l01123"></a>        SHELL_FLAG_OLF_CRLF     = (1&lt;&lt;1)
<a id="l01124"></a>};
<a id="l01125"></a>
<a id="l01129"></a>struct shell {
<a id="l01131"></a>        const char *default_prompt;
<a id="l01132"></a>
<a id="l01133"></a>        const struct shell_transport *iface;
<a id="l01134"></a>        struct shell_ctx *ctx;
<a id="l01135"></a>
<a id="l01136"></a>        struct shell_history *history;
<a id="l01137"></a>
<a id="l01138"></a>        const enum shell_flag shell_flag;
<a id="l01139"></a>
<a id="l01140"></a>        const struct shell_fprintf *fprintf_ctx;
<a id="l01141"></a>
<a id="l01142"></a>        struct shell_stats *stats;
<a id="l01143"></a>
<a id="l01144"></a>        const struct shell_log_backend *log_backend;
<a id="l01145"></a>
<a id="l01146"></a>        LOG_INSTANCE_PTR_DECLARE(log);
<a id="l01147"></a>
<a id="l01148"></a>        const char *name;
<a id="l01149"></a>        struct k_thread *thread;
<a id="l01150"></a>        k_thread_stack_t *stack;
<a id="l01152"></a>};
<a id="l01153"></a>
<a id="l01154"></a>extern void z_shell_print_stream(const void *user_ctx, const char *data,
<a id="l01155"></a>                                 size_t data_len);
<a id="l01156"></a>
<a id="l01169"></a>#define Z_SHELL_DEFINE(_name, _prompt, _transport_iface, _out_buf, _log_backend, _shell_flag)      \
<a id="l01170"></a>        static const struct shell _name;                                                           \
<a id="l01171"></a>        static struct shell_ctx UTIL_CAT(_name, _ctx);                                             \
<a id="l01172"></a>        Z_SHELL_HISTORY_DEFINE(_name##_history, CONFIG_SHELL_HISTORY_BUFFER);                      \
<a id="l01173"></a>        Z_SHELL_FPRINTF_DEFINE(_name##_fprintf, &amp;_name, _out_buf, CONFIG_SHELL_PRINTF_BUFF_SIZE,   \
<a id="l01174"></a>                               IS_ENABLED(CONFIG_SHELL_PRINTF_AUTOFLUSH), z_shell_print_stream);   \
<a id="l01175"></a>        LOG_INSTANCE_REGISTER(shell, _name, CONFIG_SHELL_LOG_LEVEL);                               \
<a id="l01176"></a>        Z_SHELL_STATS_DEFINE(_name);                                                               \
<a id="l01177"></a>        static K_KERNEL_STACK_DEFINE(_name##_stack, CONFIG_SHELL_STACK_SIZE);                      \
<a id="l01178"></a>        static struct k_thread _name##_thread;                                                     \
<a id="l01179"></a>        static const STRUCT_SECTION_ITERABLE(shell, _name) = {                                     \
<a id="l01180"></a>                .default_prompt = _prompt,                                                         \
<a id="l01181"></a>                .iface = _transport_iface,                                                         \
<a id="l01182"></a>                .ctx = &amp;UTIL_CAT(_name, _ctx),                                                     \
<a id="l01183"></a>                .history = IS_ENABLED(CONFIG_SHELL_HISTORY) ? &amp;_name##_history : NULL,             \
<a id="l01184"></a>                .shell_flag = _shell_flag,                                                         \
<a id="l01185"></a>                .fprintf_ctx = &amp;_name##_fprintf,                                                   \
<a id="l01186"></a>                .stats = Z_SHELL_STATS_PTR(_name),                                                 \
<a id="l01187"></a>                .log_backend = _log_backend,                                                       \
<a id="l01188"></a>                LOG_INSTANCE_PTR_INIT(log, shell, _name).name =                                    \
<a id="l01189"></a>                        STRINGIFY(_name), .thread = &amp;_name##_thread, .stack = _name##_stack}
<a id="l01190"></a>
<a id="l01204"></a>#define SHELL_DEFINE(_name, _prompt, _transport_iface, _log_queue_size, _log_timeout, _shell_flag) \
<a id="l01205"></a>        static uint8_t _name##_out_buffer[CONFIG_SHELL_PRINTF_BUFF_SIZE];                          \
<a id="l01206"></a>        Z_SHELL_LOG_BACKEND_DEFINE(_name, _name##_out_buffer, CONFIG_SHELL_PRINTF_BUFF_SIZE,       \
<a id="l01207"></a>                                   _log_queue_size, _log_timeout);                                 \
<a id="l01208"></a>        Z_SHELL_DEFINE(_name, _prompt, _transport_iface, _name##_out_buffer,                       \
<a id="l01209"></a>                       Z_SHELL_LOG_BACKEND_PTR(_name), _shell_flag)
<a id="l01210"></a>
<a id="l01224"></a>int shell_init(const struct shell *sh, const void *transport_config,
<a id="l01225"></a>               struct shell_backend_config_flags cfg_flags,
<a id="l01226"></a>               bool log_backend, uint32_t init_log_level);
<a id="l01227"></a>
<a id="l01234"></a>void shell_uninit(const struct shell *sh, shell_uninit_cb_t cb);
<a id="l01235"></a>
<a id="l01243"></a>int shell_start(const struct shell *sh);
<a id="l01244"></a>
<a id="l01255"></a>int shell_stop(const struct shell *sh);
<a id="l01256"></a>
<a id="l01260"></a>#define SHELL_NORMAL    SHELL_VT100_COLOR_DEFAULT
<a id="l01261"></a>
<a id="l01265"></a>#define SHELL_INFO      SHELL_VT100_COLOR_GREEN
<a id="l01266"></a>
<a id="l01270"></a>#define SHELL_OPTION    SHELL_VT100_COLOR_CYAN
<a id="l01271"></a>
<a id="l01275"></a>#define SHELL_WARNING   SHELL_VT100_COLOR_YELLOW
<a id="l01276"></a>
<a id="l01280"></a>#define SHELL_ERROR     SHELL_VT100_COLOR_RED
<a id="l01281"></a>
<a id="l01282"></a>#ifdef CONFIG_SHELL_REMOTE_CLI
<a id="l01283"></a>#include &lt;zephyr/shell/shell_remote_cli.h&gt;
<a id="l01284"></a>#endif
<a id="l01285"></a>
<a id="l01287"></a>void __printf_like(3, 4) shell_fprintf_impl(const struct shell *sh, enum shell_vt100_color color,
<a id="l01288"></a>                                            const char *fmt, ...);
<a id="l01290"></a>
<a id="l01303"></a>#define shell_fprintf(sh, color, fmt, ...)                                                         \
<a id="l01304"></a>        COND_CODE_1(IS_ENABLED(CONFIG_SHELL_REMOTE_CLI), \
<a id="l01305"></a>                (SHELL_REMOTE_CLI_FPRINTF(sh, color, fmt, ##__VA_ARGS__)), \
<a id="l01306"></a>                (shell_fprintf_impl(sh, color, fmt, ##__VA_ARGS__)))
<a id="l01307"></a>
<a id="l01320"></a>void shell_vfprintf(const struct shell *sh, enum shell_vt100_color color,
<a id="l01321"></a>                   const char *fmt, va_list args);
<a id="l01322"></a>
<a id="l01333"></a>void shell_cbpprintf(const struct shell *sh, enum shell_vt100_color color, void *package);
<a id="l01334"></a>
<a id="l01350"></a>void shell_hexdump_line(const struct shell *sh, unsigned int offset,
<a id="l01351"></a>                        const uint8_t *data, size_t len);
<a id="l01352"></a>
<a id="l01360"></a>void shell_hexdump(const struct shell *sh, const uint8_t *data, size_t len);
<a id="l01361"></a>
<a id="l01371"></a>#define shell_info(_sh, _ft, ...)        shell_fprintf(_sh, SHELL_INFO, _ft "\n", ##__VA_ARGS__)
<a id="l01372"></a>
<a id="l01382"></a>#define shell_fprintf_info(_sh, _ft, ...) shell_fprintf(_sh, SHELL_INFO, _ft, ##__VA_ARGS__)
<a id="l01383"></a>
<a id="l01393"></a>#define shell_print(_sh, _ft, ...)         shell_fprintf_normal(_sh, _ft "\n", ##__VA_ARGS__)
<a id="l01394"></a>
<a id="l01404"></a>#define shell_fprintf_normal(_sh, _ft, ...) shell_fprintf(_sh, SHELL_NORMAL, _ft, ##__VA_ARGS__)
<a id="l01405"></a>
<a id="l01415"></a>#define shell_warn(_sh, _ft, ...)        shell_fprintf_warn(_sh, _ft "\n", ##__VA_ARGS__)
<a id="l01416"></a>
<a id="l01426"></a>#define shell_fprintf_warn(_sh, _ft, ...) shell_fprintf(_sh, SHELL_WARNING, _ft, ##__VA_ARGS__)
<a id="l01427"></a>
<a id="l01437"></a>#define shell_error(_sh, _ft, ...)        shell_fprintf_error(_sh, _ft "\n", ##__VA_ARGS__)
<a id="l01438"></a>
<a id="l01448"></a>#define shell_fprintf_error(_sh, _ft, ...) shell_fprintf(_sh, SHELL_ERROR, _ft, ##__VA_ARGS__)
<a id="l01449"></a>
<a id="l01456"></a>void shell_process(const struct shell *sh);
<a id="l01457"></a>
<a id="l01467"></a>int shell_prompt_change(const struct shell *sh, const char *prompt);
<a id="l01468"></a>
<a id="l01477"></a>#ifdef CONFIG_SHELL_HELP
<a id="l01478"></a>void shell_help(const struct shell *sh);
<a id="l01479"></a>#else
<a id="l01480"></a>static inline void shell_help(const struct shell *sh)
<a id="l01481"></a>{
<a id="l01482"></a>        ARG_UNUSED(sh);
<a id="l01483"></a>}
<a id="l01484"></a>#endif /* CONFIG_SHELL_HELP */
<a id="l01485"></a>
<a id="l01487"></a>#define SHELL_CMD_HELP_PRINTED  (1)
<a id="l01488"></a>
<a id="l01506"></a>int shell_execute_cmd(const struct shell *sh, const char *cmd);
<a id="l01507"></a>
<a id="l01519"></a>int shell_set_root_cmd(const char *cmd);
<a id="l01520"></a>
<a id="l01530"></a>void shell_set_bypass(const struct shell *sh, shell_bypass_cb_t bypass, void *user_data);
<a id="l01531"></a>
<a id="l01539"></a>bool shell_ready(const struct shell *sh);
<a id="l01540"></a>
<a id="l01551"></a>int shell_insert_mode_set(const struct shell *sh, bool val);
<a id="l01552"></a>
<a id="l01564"></a>int shell_use_colors_set(const struct shell *sh, bool val);
<a id="l01565"></a>
<a id="l01576"></a>int shell_use_vt100_set(const struct shell *sh, bool val);
<a id="l01577"></a>
<a id="l01588"></a>int shell_echo_set(const struct shell *sh, bool val);
<a id="l01589"></a>
<a id="l01601"></a>int shell_obscure_set(const struct shell *sh, bool obscure);
<a id="l01602"></a>
<a id="l01614"></a>int shell_mode_delete_set(const struct shell *sh, bool val);
<a id="l01615"></a>
<a id="l01623"></a>int shell_get_return_value(const struct shell *sh);
<a id="l01624"></a>
<a id="l01636"></a>void shell_readline_prompt_set(const struct shell *sh, const char *prompt);
<a id="l01637"></a>
<a id="l01663"></a>int shell_readline(const struct shell *sh, uint8_t *buf, size_t len, k_timeout_t timeout);
<a id="l01664"></a>
<a id="l01668"></a>
<a id="l01669"></a>#ifdef __cplusplus
<a id="l01670"></a>}
<a id="l01671"></a>#endif
<a id="l01672"></a>
<a id="l01673"></a>#ifdef CONFIG_SHELL_CUSTOM_HEADER
<a id="l01674"></a>/* This include must always be at the end of shell.h */
<a id="l01675"></a>#include &lt;zephyr_custom_shell.h&gt;
<a id="l01676"></a>#endif
<a id="l01677"></a>
<a id="l01678"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_H_ */
</code></pre>

## 3.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2018 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. 将条目添加到内存段（Memory Section）时，64位构建的POSIX架构和x86_64目标会应用填充。这里加入填充，以便将该段中的数据作为数组处理。

3. CONFIG_SHELL_HELP条件编译结束标记。

4. 用于创建字典命令处理函数（Dictionary Command Handlers）的内部宏。

5. 用于创建字典命令（Dictionary Commands）的内部宏。

6. CONFIG_SHELL_STATS条件编译结束标记。

7. CONFIG_SHELL_HELP条件编译结束标记。

8. 此包含指令必须始终放在shell.h的末尾。

9. ZEPHYR_INCLUDE_SHELL_SHELL_H_头文件包含保护结束。

## 3.3\_原页符号提示（Symbol Descriptions）

### `k_thread_stack_t`

```c
struct z_thread_stack_element k_thread_stack_t
```

struct z_thread_stack_element的类型定义（Typedef）。

定义位置（Definition）：arch_interface.h:46。

符号定位：[k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)。

### `atomic_t`

```c
long atomic_t
```

原子整型变量（Atomic Integer Variable）。

定义位置（Definition）：atomic_types.h:34。

符号定位：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)。

### `cmd`

```c
static void cmd(uint32_t command)
```

通过协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。（保留原网页自动关联的符号提示；这不是Shell核心功能说明。）

定义位置（Definition）：ft8xx_reference_api.h:153。

符号定位：[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

### `LOG_INSTANCE_PTR_DECLARE`

```c
#define LOG_INSTANCE_PTR_DECLARE(_name)
```

在模块结构中声明日志记录器实例指针（Logger Instance Pointer）。

定义位置（Definition）：log_instance.h:154。

符号定位：[LOG_INSTANCE_PTR_DECLARE](../log_core_reference/P002_日志公共接口.md#ga224e4a75dca6d1b363ef49e96730dcfd)。

### `shell_readline`

```c
int shell_readline(const struct shell *sh, uint8_t *buf, size_t len, k_timeout_t timeout)
```

从Shell读取一行输入。

符号定位：[shell_readline](P001_Shell核心接口.md#ga05b2eb80f3484216ef2e1d4bf9492453)。

### `shell_help_is_structured`

```c
static bool shell_help_is_structured(const char *help)
```

检查帮助字符串是否为结构化帮助（Structured Help）。

定义位置（Definition）：shell.h:345。

符号定位：[shell_help_is_structured](P001_Shell核心接口.md#ga061bf2530269ebf20d8e006dace5e33b)。

### `shell_uninit`

```c
void shell_uninit(const struct shell *sh, shell_uninit_cb_t cb)
```

反初始化传输层和Shell内部状态。

符号定位：[shell_uninit](P001_Shell核心接口.md#ga07e76646c5065218464aa8ce78b75af3)。

### `shell_uninit_cb_t`

```c
void(* shell_uninit_cb_t)(const struct shell *sh, int res)
```

Shell反初始化完成回调（Uninitialization Completion Callback）。

定义位置（Definition）：shell.h:844。

符号定位：[shell_uninit_cb_t](P001_Shell核心接口.md#ga0844a0ce151551d3ccf45d507e5bab25)。

### `shell_hexdump_line`

```c
void shell_hexdump_line(const struct shell *sh, unsigned int offset, const uint8_t *data, size_t len)
```

以十六进制格式（Hexadecimal Format）打印一行数据。

符号定位：[shell_hexdump_line](P001_Shell核心接口.md#ga0b6e69b499c153ae8f7ba256d445f09d)。

### `shell_dict_cmd_handler`

```c
int(* shell_dict_cmd_handler)(const struct shell *sh, size_t argc, char **argv, void *data)
```

Shell字典命令处理函数原型（Dictionary Command Handler Prototype）。

定义位置（Definition）：shell.h:283。

符号定位：[shell_dict_cmd_handler](P001_Shell核心接口.md#ga182f247052041f1236d13726589885e2)。

### `shell_fprintf`

```c
#define shell_fprintf(sh, color, fmt,...)
```

类似printf的函数，向Shell发送格式化数据流（Formatted Data Stream）。

定义位置（Definition）：shell.h:1303。

符号定位：[shell_fprintf](P001_Shell核心接口.md#ga1fd1671311b112f0c87ab2dafd801105)。

### `shell_prompt_change`

```c
int shell_prompt_change(const struct shell *sh, const char *prompt)
```

更改显示的Shell提示符（Prompt）。

符号定位：[shell_prompt_change](P001_Shell核心接口.md#ga2113b7227b155755a7ab8a928f7ae499)。

### `shell_transport_handler_t`

```c
void(* shell_transport_handler_t)(enum shell_transport_evt evt, void *context)
```

Shell传输事件处理回调（Transport Event Handler Callback）。

定义位置（Definition）：shell.h:831。

符号定位：[shell_transport_handler_t](P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

### `shell_mode_delete_set`

```c
int shell_mode_delete_set(const struct shell *sh, bool val)
```

允许应用控制Delete键执行退格（Backspace）还是删除（Delete）。

符号定位：[shell_mode_delete_set](P001_Shell核心接口.md#ga2df2997c4b04f3246c22f43b274a353b)。

### `shell_readline_prompt_set`

```c
void shell_readline_prompt_set(const struct shell *sh, const char *prompt)
```

为下一次shell_readline调用设置提示字符串（Prompt String）。

符号定位：[shell_readline_prompt_set](P001_Shell核心接口.md#ga313068db9c3b9972ca4129085d8605d5)。

### `shell_cmd_handler`

```c
int(* shell_cmd_handler)(const struct shell *sh, size_t argc, char **argv)
```

Shell命令处理函数原型（Command Handler Prototype）。

定义位置（Definition）：shell.h:267。

符号定位：[shell_cmd_handler](P001_Shell核心接口.md#ga331e7d19b9b0755486596f5ffc598338)。

### `shell_set_bypass`

```c
void shell_set_bypass(const struct shell *sh, shell_bypass_cb_t bypass, void *user_data)
```

设置旁路回调（Bypass Callback）。

符号定位：[shell_set_bypass](P001_Shell核心接口.md#ga4d51d4dbb22bed5d040deabc7ab6dc9d)。

### `shell_get_return_value`

```c
int shell_get_return_value(const struct shell *sh)
```

取得最近一次执行的Shell命令的返回值。

符号定位：[shell_get_return_value](P001_Shell核心接口.md#ga54dc053c92641bc9b9736bc2d61140f7)。

### `shell_flag`

```c
shell_flag
```

设置Shell输出换行序列（Output Newline Sequence）的标志。

定义位置（Definition）：shell.h:1121。

符号定位：[shell_flag](P001_Shell核心接口.md#ga56bf30741f9ec7a6d94e5c18c2858948)。

### `shell_device_lookup`

```c
const struct device * shell_device_lookup(size_t idx, const char *prefix)
```

按索引取得匹配的设备。（原文在matches后未给出匹配对象，参数说明见下文。）

符号定位：[shell_device_lookup](P001_Shell核心接口.md#ga571db3aa3e024a09e82b117a74d6f248)。

### `shell_vt100_color`

```c
shell_vt100_color
```

Shell输出可用的文本颜色（Text Colors）。

定义位置（Definition）：shell_types.h:27。

符号定位：[shell_vt100_color](P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)。

### `shell_cbpprintf`

```c
void shell_cbpprintf(const struct shell *sh, enum shell_vt100_color color, void *package)
```

将cbprintf包格式化后以数据流形式发送到Shell的函数。

符号定位：[shell_cbpprintf](P001_Shell核心接口.md#ga706aebd24cbdb7f14b9a324515414ecf)。

### `shell_vfprintf`

```c
void shell_vfprintf(const struct shell *sh, enum shell_vt100_color color, const char *fmt, va_list args)
```

类似vprintf的函数，向Shell发送格式化数据流。

符号定位：[shell_vfprintf](P001_Shell核心接口.md#ga74a1c4edd803cad14c893fc9816e534f)。

### `shell_set_root_cmd`

```c
int shell_set_root_cmd(const char *cmd)
```

为所有Shell实例设置根命令（Root Command）。

符号定位：[shell_set_root_cmd](P001_Shell核心接口.md#ga768c606f2d50f24e9b607ba0a341686d)。

### `shell_ready`

```c
bool shell_ready(const struct shell *sh)
```

取得Shell是否已就绪、能够执行命令的状态。

符号定位：[shell_ready](P001_Shell核心接口.md#ga79369ddfea2dc2cb5813c5eb5c67634a)。

### `shell_use_colors_set`

```c
int shell_use_colors_set(const struct shell *sh, bool val)
```

允许应用控制终端输出是否使用彩色语法（Colored Syntax）。

符号定位：[shell_use_colors_set](P001_Shell核心接口.md#ga7d5873456ba43ebd3cc86d25e3f4a72c)。

### `shell_process`

```c
void shell_process(const struct shell *sh)
```

传输接口中有数据就绪时应执行的处理函数（Process Function）。

符号定位：[shell_process](P001_Shell核心接口.md#ga7e66389d0faf15a2a7c31c68cdd9c36c)。

### `shell_device_get_binding`

```c
const struct device * shell_device_get_binding(const char *name)
```

通过device::name字段或标签（Label）取得设备引用。

符号定位：[shell_device_get_binding](P001_Shell核心接口.md#ga7fb40045dc0a27c175e37a6c9cd84b53)。

### `shell_use_vt100_set`

```c
int shell_use_vt100_set(const struct shell *sh, bool val)
```

允许应用控制终端是否使用VT100命令。

符号定位：[shell_use_vt100_set](P001_Shell核心接口.md#ga80ff4b3b4cc62e543fd510c14f55b42a)。

### `shell_obscure_set`

```c
int shell_obscure_set(const struct shell *sh, bool obscure)
```

允许应用控制是否用星号遮蔽用户输入，可用于实现……（原符号提示在此截断）

符号定位：[shell_obscure_set](P001_Shell核心接口.md#ga86fade2757d04c9220d5912a4ee540a0)。

### `shell_init`

```c
int shell_init(const struct shell *sh, const void *transport_config, struct shell_backend_config_flags cfg_flags, bool log_backend, uint32_t init_log_level)
```

初始化传输层（Transport Layer）和Shell内部状态的函数。

符号定位：[shell_init](P001_Shell核心接口.md#ga8764ff11603855a10419c48e46e8221c)。

### `shell_device_lookup_all`

```c
const struct device * shell_device_lookup_all(size_t idx, const char *prefix)
```

按索引取得匹配的设备。（原文在matches后未给出匹配对象，参数说明见下文。）

符号定位：[shell_device_lookup_all](P001_Shell核心接口.md#ga8e83709f5e75d4cea51f42f41bb4e20f)。

### `shell_device_get_binding_all`

```c
const struct device * shell_device_get_binding_all(const char *name)
```

通过device::name字段或标签（Label）取得设备引用。

符号定位：[shell_device_get_binding_all](P001_Shell核心接口.md#ga919147e222fe10ce14ab3c3a5c5a94e3)。

### `shell_help`

```c
static void shell_help(const struct shell *sh)
```

打印当前命令的帮助。

定义位置（Definition）：shell.h:1480。

符号定位：[shell_help](P001_Shell核心接口.md#ga9e4911ff2c3a07fa70711ddac83701d6)。

### `shell_device_lookup_non_ready`

```c
const struct device * shell_device_lookup_non_ready(size_t idx, const char *prefix)
```

按索引取得匹配的、未初始化设备。（原文在matches后未给出匹配对象，参数说明见下文。）

符号定位：[shell_device_lookup_non_ready](P001_Shell核心接口.md#ga9f2994f2d6a55521a3e162a81299e4c3)。

### `shell_device_filter_t`

```c
bool(* shell_device_filter_t)(const struct device *dev)
```

用于shell_device_filter的过滤回调类型（Filter Callback Type）。

定义位置（Definition）：shell.h:198。

符号定位：[shell_device_filter_t](P001_Shell核心接口.md#gaa2b8cf8ac78b8355408ef94958ebdc70)。

### `shell_execute_cmd`

```c
int shell_execute_cmd(const struct shell *sh, const char *cmd)
```

执行命令（Execute Command）。

符号定位：[shell_execute_cmd](P001_Shell核心接口.md#gabfb6a1f1f53f90365de349348015311e)。

### `shell_bypass_cb_t`

```c
void(* shell_bypass_cb_t)(const struct shell *sh, uint8_t *data, size_t len, void *user_data)
```

旁路回调（Bypass Callback）。

定义位置（Definition）：shell.h:853。

符号定位：[shell_bypass_cb_t](P001_Shell核心接口.md#gacaddbcd6e84f377f39a5d69398996557)。

### `shell_stop`

```c
int shell_stop(const struct shell *sh)
```

停止Shell处理的函数。

符号定位：[shell_stop](P001_Shell核心接口.md#gad27754d0beb31bc501f28f9ef26a362c)。

### `shell_start`

```c
int shell_start(const struct shell *sh)
```

启动Shell处理的函数。

符号定位：[shell_start](P001_Shell核心接口.md#gad386d4e8077103e7976f25996fcc3132)。

### `shell_echo_set`

```c
int shell_echo_set(const struct shell *sh, bool val)
```

允许应用控制是否回显用户输入（Echo）。

符号定位：[shell_echo_set](P001_Shell核心接口.md#gad53881371bbaedfd3ef3ecf219706fd1)。

### `shell_device_filter`

```c
const struct device * shell_device_filter(size_t idx, shell_device_filter_t filter)
```

根据索引与过滤器（Filter）取得设备。

符号定位：[shell_device_filter](P001_Shell核心接口.md#gae2a8e3d44a9bf5eb55be80833ac6eb5d)。

### `shell_hexdump`

```c
void shell_hexdump(const struct shell *sh, const uint8_t *data, size_t len)
```

以十六进制格式打印数据。

符号定位：[shell_hexdump](P001_Shell核心接口.md#gaeeba0b483974205c54e364d509badd42)。

### `shell_insert_mode_set`

```c
int shell_insert_mode_set(const struct shell *sh, bool val)
```

允许应用控制文本插入模式（Insert Mode）。

符号定位：[shell_insert_mode_set](P001_Shell核心接口.md#gaf1f41d8b6cd430357d593ab0fc5adfeb)。

### `shell_dynamic_get`

```c
void(* shell_dynamic_get)(size_t idx, struct shell_static_entry *entry)
```

Shell动态命令描述符（Dynamic Command Descriptor）。

定义位置（Definition）：shell.h:103。

符号定位：[shell_dynamic_get](P001_Shell核心接口.md#gafc042f32bac2fdd4cbde9f943e29b008)。

### `SHELL_FLAG_CRLF_DEFAULT`

```c
@ SHELL_FLAG_CRLF_DEFAULT
```

不转换回车（CR）或换行（LF）。

定义位置（Definition）：shell.h:1122。

符号定位：[SHELL_FLAG_CRLF_DEFAULT](P001_Shell核心接口.md#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab)。

### `SHELL_FLAG_OLF_CRLF`

```c
@ SHELL_FLAG_OLF_CRLF
```

输出时将LF转换为CRLF。

定义位置（Definition）：shell.h:1123。

符号定位：[SHELL_FLAG_OLF_CRLF](P001_Shell核心接口.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446)。

### `BIT`

```c
#define BIT(n)
```

第n位被置位的无符号整数（Unsigned Integer），在汇编语言中为有符号形式。

定义位置（Definition）：util_macro.h:44。

符号定位：[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

### `k_tid_t`

```c
struct k_thread * k_tid_t
```

定义位置（Definition）：thread.h:414。

符号定位：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)。

### `kernel.h`

公共内核 API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `log.h`

日志子系统（Logging Subsystem）的头文件。

符号定位：[log.h](../log_core_reference/P003_日志公共头文件参考.md)。

### `log_instance.h`

日志实例注册（Log Instance Registration）的头文件。

符号定位：[log_instance.h](../log_internal_reference/P003_日志实例头文件参考.md)。

### `flags`

```c
flags
```

定义位置（Definition）：parser.h:86。

符号定位：[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

### `state`

```c
state
```

定义位置（Definition）：parser_state.h:29。

符号定位：[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

### `shell_fprintf.h`

Shell格式化输出辅助函数（Formatted Output Helpers）的头文件。

符号定位：[shell_fprintf.h](../shell_util_reference/P001_Shell格式化输出头文件参考.md)。

### `shell_history.h`

Shell命令历史（Command History）的头文件。

符号定位：[shell_history.h](../shell_util_reference/P003_Shell命令历史头文件参考.md)。

### `shell_log_backend.h`

Shell日志后端（Log Backend）的头文件。

符号定位：[shell_log_backend.h](../shell_backend_reference/P013_Shell日志后端头文件参考.md)。

### `shell_remote_cli.h`

远端Shell客户端（Remote Shell Client）的API。

符号定位：[shell_remote_cli.h](../shell_remote_reference/P004_远端Shell命令行头文件参考.md)。

### `shell_string_conv.h`

Shell字符串转换辅助函数（String Conversion Helpers）的头文件。

符号定位：[shell_string_conv.h](../shell_util_reference/P005_Shell字符串转换头文件参考.md)。

### `shell_types.h`

Shell终端类型与颜色（Terminal Types and Colors）的头文件。

符号定位：[shell_types.h](../shell_util_reference/P007_Shell类型头文件参考.md)。

### `bool`

```c
#define bool
```

定义位置（Definition）：stdbool.h:13。

符号定位：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `device`

每个驱动实例的运行时设备结构（Runtime Device Structure），位于ROM中。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `device::name`

```c
const char * name
```

设备实例名称（Device Instance Name）。

定义位置（Definition）：device.h:545。

符号定位：[device::name](../device_reference/P002_设备对象结构.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)。

### `k_event`

事件结构（Event Structure）。

定义位置（Definition）：kernel.h:2695。

符号定位：[k_event](../eventpoll_reference/P002_内核事件结构.md)。

### `k_sem`

信号量结构（Semaphore Structure）。

定义位置（Definition）：kernel.h:3738。

符号定位：[k_sem](../synchronization_reference/P009_内核信号量结构.md)。

### `k_thread`

线程结构（Thread Structure）。

定义位置（Definition）：thread.h:258。

符号定位：[k_thread](../thread_core_reference/P004_线程对象结构.md)。

### `k_timeout_t`

内核超时类型（Kernel Timeout Type）。

定义位置（Definition）：clock.h:65。

符号定位：[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

### `log_backend_api`

日志记录器后端API（Logger Backend API）。

定义位置（Definition）：log_backend.h:74。

符号定位：[log_backend_api](../log_backend_reference/P005_日志后端操作表.md)。

### `log_backend`

日志记录器后端结构（Logger Backend Structure）。

定义位置（Definition）：log_backend.h:118。

符号定位：[log_backend](../log_backend_reference/P004_日志后端结构.md)。

### `shell_cmd_help`

Shell结构化帮助描述符（Structured Help Descriptor）。

定义位置（Definition）：shell.h:317。

符号定位：[shell_cmd_help](P006_Shell命令帮助结构.md)。

### `shell_cmd_help::usage`

```c
const char * usage
```

命令用法字符串（Command Usage String）。

定义位置（Definition）：shell.h:322。

符号定位：[shell_cmd_help::usage](P006_Shell命令帮助结构.md#a3735f4afeeea3d968d9e8fc74e0aa68f)。

### `shell_cmd_help::description`

```c
const char * description
```

命令描述（Command Description）。

定义位置（Definition）：shell.h:321。

符号定位：[shell_cmd_help::description](P006_Shell命令帮助结构.md#af9e182e1599c3cfcc42f739d40a511bb)。

### `shell_ctx`

Shell实例上下文（Instance Context）。

定义位置（Definition）：shell.h:1043。

符号定位：[shell_ctx](P005_Shell运行上下文.md)。

### `shell_static_args`

Shell命令的参数数量约束（Argument Count Constraints）与远端路由（Remote Routing）。

定义位置（Definition）：shell.h:120。

符号定位：[shell_static_args](P007_Shell命令参数约束.md)。

### `shell_static_args::remote_id`

```c
uint16_t remote_id
```

远端连接编号（Remote Connection ID）；仅在remote_cmd非零时有效。

定义位置（Definition）：shell.h:124。

符号定位：[shell_static_args::remote_id](P007_Shell命令参数约束.md#a21f53604a733e4351687a71d45909abd)。

### `shell_static_args::remote_cmd`

```c
uint16_t remote_cmd
```

远端Shell命令类型（Remote Command Type）；远端Shell对应非零值。

定义位置（Definition）：shell.h:123。

符号定位：[shell_static_args::remote_cmd](P007_Shell命令参数约束.md#a2b3bab087c7f7bed6217df86d6577925)。

### `shell_static_args::mandatory`

```c
uint8_t mandatory
```

必需参数数量（Mandatory Argument Count）。

定义位置（Definition）：shell.h:121。

符号定位：[shell_static_args::mandatory](P007_Shell命令参数约束.md#a2c23bfa755d3bb651e299ff461065d98)。

### `shell_static_args::optional`

```c
uint8_t optional
```

可选参数（Optional Arguments）的数量。

定义位置（Definition）：shell.h:122。

符号定位：[shell_static_args::optional](P007_Shell命令参数约束.md#aa3aa836ed537dde38e64d2c677ace5ae)。

### `shell_static_entry`

Shell静态命令描述符（Static Command Descriptor）。

定义位置（Definition）：shell.h:299。

符号定位：[shell_static_entry](P008_Shell静态命令条目.md)。

### `shell_static_entry::subcmd`

```c
const union shell_cmd_entry * subcmd
```

子命令指针（Subcommand Pointer）。

定义位置（Definition）：shell.h:302。

符号定位：[shell_static_entry::subcmd](P008_Shell静态命令条目.md#a14534428d81f5ffeb303a5320766cd0a)。

### `shell_static_entry::handler`

```c
shell_cmd_handler handler
```

命令处理函数（Command Handler）。

定义位置（Definition）：shell.h:303。

符号定位：[shell_static_entry::handler](P008_Shell静态命令条目.md#a3147eb0cc1fea698dd433127acb1f220)。

### `shell_static_entry::args`

```c
struct shell_static_args args
```

命令参数（Command Arguments）。

定义位置（Definition）：shell.h:304。

符号定位：[shell_static_entry::args](P008_Shell静态命令条目.md#a73951d31712342c0c0545a142059d367)。

### `shell_static_entry::help`

```c
const char * help
```

命令帮助字符串（Command Help String）。

定义位置（Definition）：shell.h:301。

符号定位：[shell_static_entry::help](P008_Shell静态命令条目.md#ac8fb0fc23957a49d9a3664b5baa08704)。

### `shell_static_entry::syntax`

```c
const char * syntax
```

命令语法字符串（Command Syntax Strings）。

定义位置（Definition）：shell.h:300。

符号定位：[shell_static_entry::syntax](P008_Shell静态命令条目.md#ad87defa749ee7481f6d29d8c9084fb91)。

### `shell_transport_api`

统一的Shell传输接口（Transport Interface）。

定义位置（Definition）：shell.h:864。

符号定位：[shell_transport_api](P010_Shell传输接口结构.md)。

### `shell_transport_api::update`

```c
void(* update)(const struct shell_transport *transport)
```

在Shell线程循环中调用的函数。

定义位置（Definition）：shell.h:938。

符号定位：[shell_transport_api::update](P010_Shell传输接口结构.md#a3b447d16d7c30f994c582d67bde57ba8)。

### `shell_transport_api::init`

```c
int(* init)(const struct shell_transport *transport, const void *config, shell_transport_handler_t evt_handler, void *context)
```

初始化Shell传输接口的函数。

定义位置（Definition）：shell.h:876。

符号定位：[shell_transport_api::init](P010_Shell传输接口结构.md#a59afba962312a077343b440448d67135)。

### `shell_transport_api::write`

```c
int(* write)(const struct shell_transport *transport, const void *data, size_t length, size_t *cnt)
```

向传输接口写入数据的函数。

定义位置（Definition）：shell.h:915。

符号定位：[shell_transport_api::write](P010_Shell传输接口结构.md#a6bbf2905abcbf6ca564ecf3f07d95712)。

### `shell_transport_api::uninit`

```c
int(* uninit)(const struct shell_transport *transport)
```

反初始化Shell传输接口的函数。

定义位置（Definition）：shell.h:888。

符号定位：[shell_transport_api::uninit](P010_Shell传输接口结构.md#a94cc7843174a4aba668389a4b46928d3)。

### `shell_transport_api::enable`

```c
int(* enable)(const struct shell_transport *transport, bool blocking_tx)
```

以给定发送（TX）模式启用传输的函数。

定义位置（Definition）：shell.h:902。

符号定位：[shell_transport_api::enable](P010_Shell传输接口结构.md#a95535c7195088e68230ecb306f105713)。

### `shell_transport_api::read`

```c
int(* read)(const struct shell_transport *transport, void *data, size_t length, size_t *cnt)
```

从传输接口读取数据的函数。

定义位置（Definition）：shell.h:928。

符号定位：[shell_transport_api::read](P010_Shell传输接口结构.md#aae0e8ad92065dbff10691c28045d0c8f)。

### `shell_transport`

Shell传输实例（Transport Instance）。

定义位置（Definition）：shell.h:949。

符号定位：[shell_transport](P009_Shell传输实例.md)。

### `shell_transport::ctx`

```c
void * ctx
```

传输实例上下文（Transport Instance Context）。

定义位置（Definition）：shell.h:951。

符号定位：[shell_transport::ctx](P009_Shell传输实例.md#a02f44bb376152452f5b5d20f33ccbdf6)。

### `shell_transport::api`

```c
const struct shell_transport_api * api
```

传输后端操作（Transport Backend Operations）。

定义位置（Definition）：shell.h:950。

符号定位：[shell_transport::api](P009_Shell传输实例.md#ab4bee270415b445ded5a8ba6e8cb3a25)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](P004_Shell实例结构.md)。

### `sys_getopt_state`

定义位置（Definition）：sys_getopt.h:16。

符号定位：[sys_getopt_state](https://docs.zephyrproject.org/latest/doxygen/html/structsys__getopt__state.html)。

### `iterable_sections.h`

可遍历段（Iterable Sections）辅助工具。

符号定位：[iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)。

### `util.h`

杂项工具（Miscellaneous Utilities）。

符号定位：[util.h](../util_reference/P002_通用工具头文件参考.md)。

### `sys_getopt.h`

符号定位：[sys_getopt.h](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html)。

### `toolchain.h`

用于抽象工具链（Toolchain）特有能力的宏。

符号定位：[toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)。

### `shell_cmd_entry`

Shell命令描述符（Command Descriptor）。

定义位置（Definition）：shell.h:109。

符号定位：[shell_cmd_entry](P011_Shell命令条目联合体.md)。

### `shell_cmd_entry::entry`

```c
const struct shell_static_entry * entry
```

静态命令数组的指针。

定义位置（Definition）：shell.h:114。

符号定位：[shell_cmd_entry::entry](P011_Shell命令条目联合体.md#a4abb8327df0e62f63432a05cc885f03d)。

### `shell_cmd_entry::dynamic_get`

```c
shell_dynamic_get dynamic_get
```

返回动态命令的函数指针。

定义位置（Definition）：shell.h:111。

符号定位：[shell_cmd_entry::dynamic_get](P011_Shell命令条目联合体.md#aa76e35866f5df37593705fd1b53e15df)。

## 3.4\_源码跟踪译注

> 译注——命令注册中的mandatory包含命令名称本身；optional可使用原文规定的特殊标志。条件宏与表达式宏控制命令是否存在，原宏展开保留，用来核对处理函数和子命令在不同配置下的去留。

> 译注——动态命令回调应按索引填入条目、保证语法名称按字母顺序排序，并在没有更多条目时将syntax设为NULL。返回指针或空条目的含义应遵守该回调协议，不能用未初始化字段代替结束标记。

> 译注——shell_execute_cmd禁止在Shell命令上下文内调用，而shell_readline要求从Shell线程的命令处理函数调用。二者调用条件不同；异步旁路（Bypass）与同步读行也有明确的互斥使用条件。

> 译注——readline提示字符串不会被复制，必须有效到读行返回；返回后提示设置会自动清除。缓冲区容量包含NUL终止字符，成功返回的长度不含该字符。

> 译注——字符串转换成功时保留err原值，应预先初始化错误变量。返回0或false既可能是有效结果，也可能是失败时的返回值，需要同时检查err。

> 译注——shell和shell_ctx原页只给出结构用途，内部字段由Doxygen隐藏；本册对应页如实保留这个公开范围，完整可见布局另见头文件源码。

> 译注——传输接口将后端操作表和实例上下文分开。read与write通过计数器返回实际接收或发送字节数，函数状态码与处理字节数不是同一概念。

> 译注——传输事件回调收到初始化时提供的不透明上下文。uninit完成回调则在Shell线程退出前调用；不能把这两种回调的生命周期和执行上下文混为一谈。

头文件定位：[include/zephyr/shell/shell.h](../../../include/zephyr/shell/shell.h)，关联实现／接口：[subsys/shell/shell.c](../../../subsys/shell/shell.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P002_Shell核心头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/shell/shell_types.h](../shell_util_reference/P007_Shell类型头文件参考.md)
- [zephyr/shell/shell_history.h](../shell_util_reference/P003_Shell命令历史头文件参考.md)
- [zephyr/shell/shell_fprintf.h](../shell_util_reference/P001_Shell格式化输出头文件参考.md)
- [zephyr/shell/shell_log_backend.h](../shell_backend_reference/P013_Shell日志后端头文件参考.md)
- [zephyr/shell/shell_string_conv.h](../shell_util_reference/P005_Shell字符串转换头文件参考.md)
- [zephyr/logging/log_instance.h](../log_internal_reference/P003_日志实例头文件参考.md)
- [zephyr/logging/log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/sys/sys_getopt.h](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html)
- [shell_static_entry](P008_Shell静态命令条目.md)
- [shell_dynamic_get](P001_Shell核心接口.md#gafc042f32bac2fdd4cbde9f943e29b008)
- [shell_cmd_entry](P011_Shell命令条目联合体.md)
- [dynamic_get](P011_Shell命令条目联合体.md#aa76e35866f5df37593705fd1b53e15df)
- [entry](P011_Shell命令条目联合体.md#a4abb8327df0e62f63432a05cc885f03d)
- [shell](P004_Shell实例结构.md)
- [shell_static_args](P007_Shell命令参数约束.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mandatory](P007_Shell命令参数约束.md#a2c23bfa755d3bb651e299ff461065d98)
- [optional](P007_Shell命令参数约束.md#aa3aa836ed537dde38e64d2c677ace5ae)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [remote_cmd](P007_Shell命令参数约束.md#a2b3bab087c7f7bed6217df86d6577925)
- [remote_id](P007_Shell命令参数约束.md#a21f53604a733e4351687a71d45909abd)
- [device](../device_reference/P002_设备对象结构.md)
- [shell_device_lookup](P001_Shell核心接口.md#ga571db3aa3e024a09e82b117a74d6f248)
- [shell_device_lookup_all](P001_Shell核心接口.md#ga8e83709f5e75d4cea51f42f41bb4e20f)
- [shell_device_lookup_non_ready](P001_Shell核心接口.md#ga9f2994f2d6a55521a3e162a81299e4c3)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [shell_device_filter_t](P001_Shell核心接口.md#gaa2b8cf8ac78b8355408ef94958ebdc70)
- [shell_device_filter](P001_Shell核心接口.md#gae2a8e3d44a9bf5eb55be80833ac6eb5d)
- [shell_device_get_binding](P001_Shell核心接口.md#ga7fb40045dc0a27c175e37a6c9cd84b53)
- [name](../device_reference/P002_设备对象结构.md#a1e74e8d3b0b1a981c67e1d0284ccac3d)
- [shell_device_get_binding_all](P001_Shell核心接口.md#ga919147e222fe10ce14ab3c3a5c5a94e3)
- [shell_cmd_handler](P001_Shell核心接口.md#ga331e7d19b9b0755486596f5ffc598338)
- [shell_dict_cmd_handler](P001_Shell核心接口.md#ga182f247052041f1236d13726589885e2)
- [syntax](P008_Shell静态命令条目.md#ad87defa749ee7481f6d29d8c9084fb91)
- [help](P008_Shell静态命令条目.md#ac8fb0fc23957a49d9a3664b5baa08704)
- [subcmd](P008_Shell静态命令条目.md#a14534428d81f5ffeb303a5320766cd0a)
- [handler](P008_Shell静态命令条目.md#a3147eb0cc1fea698dd433127acb1f220)
- [args](P008_Shell静态命令条目.md#a73951d31712342c0c0545a142059d367)
- [shell_cmd_help](P006_Shell命令帮助结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [description](P006_Shell命令帮助结构.md#af9e182e1599c3cfcc42f739d40a511bb)
- [usage](P006_Shell命令帮助结构.md#a3735f4afeeea3d968d9e8fc74e0aa68f)
- [shell_help_is_structured](P001_Shell核心接口.md#ga061bf2530269ebf20d8e006dace5e33b)
- [shell_transport_handler_t](P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [shell_uninit_cb_t](P001_Shell核心接口.md#ga0844a0ce151551d3ccf45d507e5bab25)
- [shell_bypass_cb_t](P001_Shell核心接口.md#gacaddbcd6e84f377f39a5d69398996557)
- [shell_transport](P009_Shell传输实例.md)
- [shell_transport_api](P010_Shell传输接口结构.md)
- [init](P010_Shell传输接口结构.md#a59afba962312a077343b440448d67135)
- [uninit](P010_Shell传输接口结构.md#a94cc7843174a4aba668389a4b46928d3)
- [enable](P010_Shell传输接口结构.md#a95535c7195088e68230ecb306f105713)
- [write](P010_Shell传输接口结构.md#a6bbf2905abcbf6ca564ecf3f07d95712)
- [read](P010_Shell传输接口结构.md#aae0e8ad92065dbff10691c28045d0c8f)
- [update](P010_Shell传输接口结构.md#a3b447d16d7c30f994c582d67bde57ba8)
- [api](P009_Shell传输实例.md#ab4bee270415b445ded5a8ba6e8cb3a25)
- [ctx](P009_Shell传输实例.md#a02f44bb376152452f5b5d20f33ccbdf6)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [shell_ctx](P005_Shell运行上下文.md)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [sys_getopt_state](https://docs.zephyrproject.org/latest/doxygen/html/structsys__getopt__state.html)
- [k_event](../eventpoll_reference/P002_内核事件结构.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [log_backend_api](../log_backend_reference/P005_日志后端操作表.md)
- [shell_flag](P001_Shell核心接口.md#ga56bf30741f9ec7a6d94e5c18c2858948)
- [SHELL_FLAG_CRLF_DEFAULT](P001_Shell核心接口.md#gga56bf30741f9ec7a6d94e5c18c2858948a343ee559d6259111dbab529a283b23ab)
- [SHELL_FLAG_OLF_CRLF](P001_Shell核心接口.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446)
- [shell_fprintf](P001_Shell核心接口.md#ga1fd1671311b112f0c87ab2dafd801105)
- [log_backend](../log_backend_reference/P004_日志后端结构.md)
- [LOG_INSTANCE_PTR_DECLARE](../log_core_reference/P002_日志公共接口.md#ga224e4a75dca6d1b363ef49e96730dcfd)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)
- [shell_init](P001_Shell核心接口.md#ga8764ff11603855a10419c48e46e8221c)
- [shell_uninit](P001_Shell核心接口.md#ga07e76646c5065218464aa8ce78b75af3)
- [shell_start](P001_Shell核心接口.md#gad386d4e8077103e7976f25996fcc3132)
- [shell_stop](P001_Shell核心接口.md#gad27754d0beb31bc501f28f9ef26a362c)
- [zephyr/shell/shell_remote_cli.h](../shell_remote_reference/P004_远端Shell命令行头文件参考.md)
- [shell_vt100_color](P001_Shell核心接口.md#ga6dcf569be711db32286fb1ef2dcf36d2)
- [shell_vfprintf](P001_Shell核心接口.md#ga74a1c4edd803cad14c893fc9816e534f)
- [shell_cbpprintf](P001_Shell核心接口.md#ga706aebd24cbdb7f14b9a324515414ecf)
- [shell_hexdump_line](P001_Shell核心接口.md#ga0b6e69b499c153ae8f7ba256d445f09d)
- [shell_hexdump](P001_Shell核心接口.md#gaeeba0b483974205c54e364d509badd42)
- [shell_process](P001_Shell核心接口.md#ga7e66389d0faf15a2a7c31c68cdd9c36c)
- [shell_prompt_change](P001_Shell核心接口.md#ga2113b7227b155755a7ab8a928f7ae499)
- [shell_help](P001_Shell核心接口.md#ga9e4911ff2c3a07fa70711ddac83701d6)
- [shell_execute_cmd](P001_Shell核心接口.md#gabfb6a1f1f53f90365de349348015311e)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [shell_set_root_cmd](P001_Shell核心接口.md#ga768c606f2d50f24e9b607ba0a341686d)
- [shell_set_bypass](P001_Shell核心接口.md#ga4d51d4dbb22bed5d040deabc7ab6dc9d)
- [shell_ready](P001_Shell核心接口.md#ga79369ddfea2dc2cb5813c5eb5c67634a)
- [shell_insert_mode_set](P001_Shell核心接口.md#gaf1f41d8b6cd430357d593ab0fc5adfeb)
- [shell_use_colors_set](P001_Shell核心接口.md#ga7d5873456ba43ebd3cc86d25e3f4a72c)
- [shell_use_vt100_set](P001_Shell核心接口.md#ga80ff4b3b4cc62e543fd510c14f55b42a)
- [shell_echo_set](P001_Shell核心接口.md#gad53881371bbaedfd3ef3ecf219706fd1)
- [shell_obscure_set](P001_Shell核心接口.md#ga86fade2757d04c9220d5912a4ee540a0)
- [shell_mode_delete_set](P001_Shell核心接口.md#ga2df2997c4b04f3246c22f43b274a353b)
- [shell_get_return_value](P001_Shell核心接口.md#ga54dc053c92641bc9b9736bc2d61140f7)
- [shell_readline_prompt_set](P001_Shell核心接口.md#ga313068db9c3b9972ca4129085d8605d5)
- [shell_readline](P001_Shell核心接口.md#ga05b2eb80f3484216ef2e1d4bf9492453)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

---

[上一章](P002_Shell核心头文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_Shell实例结构.md)
