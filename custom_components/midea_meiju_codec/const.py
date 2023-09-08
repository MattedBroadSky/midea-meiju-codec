DOMAIN = "midea_meiju_codec"
STORAGE_PATH = f".storage/{DOMAIN}/lua"
CONFIG_PATH = f".storage/{DOMAIN}/config"
DEVICES = "DEVICES"
CONF_ACCOUNT = "account"
CONF_HOME = "home"
CONF_KEY = "key"
CJSON_LUA = "LS0KLS0gY2pzb24ubHVhCi0tCi0tIENvcHlyaWdodCAoYykgMjAxOCByeGkKLS0KLS0gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZgotLSB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbgotLSB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvCi0tIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzCi0tIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbwotLSBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Ci0tCi0tIFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbAotLSBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgotLQotLSBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgotLSBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKLS0gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCi0tIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKLS0gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKLS0gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKLS0gU09GVFdBUkUuCi0tCgpsb2NhbCBjanNvbiA9IHsgX3ZlcnNpb24gPSAiMC4xLjEiIH0KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KLS0gRW5jb2RlCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCmxvY2FsIGVuY29kZQoKbG9jYWwgZXNjYXBlX2NoYXJfbWFwID0gewogIFsgIlxcIiBdID0gIlxcXFwiLAogIFsgIlwiIiBdID0gIlxcXCIiLAogIFsgIlxiIiBdID0gIlxcYiIsCiAgWyAiXGYiIF0gPSAiXFxmIiwKICBbICJcbiIgXSA9ICJcXG4iLAogIFsgIlxyIiBdID0gIlxcciIsCiAgWyAiXHQiIF0gPSAiXFx0IiwKfQoKbG9jYWwgZXNjYXBlX2NoYXJfbWFwX2ludiA9IHsgWyAiXFwvIiBdID0gIi8iIH0KZm9yIGssIHYgaW4gcGFpcnMoZXNjYXBlX2NoYXJfbWFwKSBkbwogIGVzY2FwZV9jaGFyX21hcF9pbnZbdl0gPSBrCmVuZAoKCmxvY2FsIGZ1bmN0aW9uIGVzY2FwZV9jaGFyKGMpCiAgcmV0dXJuIGVzY2FwZV9jaGFyX21hcFtjXSBvciBzdHJpbmcuZm9ybWF0KCJcXHUlMDR4IiwgYzpieXRlKCkpCmVuZAoKCmxvY2FsIGZ1bmN0aW9uIGVuY29kZV9uaWwodmFsKQogIHJldHVybiAibnVsbCIKZW5kCgoKbG9jYWwgZnVuY3Rpb24gZW5jb2RlX3RhYmxlKHZhbCwgc3RhY2spCiAgbG9jYWwgcmVzID0ge30KICBzdGFjayA9IHN0YWNrIG9yIHt9CgogIC0tIENpcmN1bGFyIHJlZmVyZW5jZT8KICBpZiBzdGFja1t2YWxdIHRoZW4gZXJyb3IoImNpcmN1bGFyIHJlZmVyZW5jZSIpIGVuZAoKICBzdGFja1t2YWxdID0gdHJ1ZQoKICBpZiB2YWxbMV0gfj0gbmlsIG9yIG5leHQodmFsKSA9PSBuaWwgdGhlbgogICAgLS0gVHJlYXQgYXMgYXJyYXkgLS0gY2hlY2sga2V5cyBhcmUgdmFsaWQgYW5kIGl0IGlzIG5vdCBzcGFyc2UKICAgIGxvY2FsIG4gPSAwCiAgICBmb3IgayBpbiBwYWlycyh2YWwpIGRvCiAgICAgIGlmIHR5cGUoaykgfj0gIm51bWJlciIgdGhlbgogICAgICAgIGVycm9yKCJpbnZhbGlkIHRhYmxlOiBtaXhlZCBvciBpbnZhbGlkIGtleSB0eXBlcyIpCiAgICAgIGVuZAogICAgICBuID0gbiArIDEKICAgIGVuZAogICAgaWYgbiB+PSAjdmFsIHRoZW4KICAgICAgZXJyb3IoImludmFsaWQgdGFibGU6IHNwYXJzZSBhcnJheSIpCiAgICBlbmQKICAgIC0tIEVuY29kZQogICAgZm9yIGksIHYgaW4gaXBhaXJzKHZhbCkgZG8KICAgICAgdGFibGUuaW5zZXJ0KHJlcywgZW5jb2RlKHYsIHN0YWNrKSkKICAgIGVuZAogICAgc3RhY2tbdmFsXSA9IG5pbAogICAgcmV0dXJuICJbIiAuLiB0YWJsZS5jb25jYXQocmVzLCAiLCIpIC4uICJdIgoKICBlbHNlCiAgICAtLSBUcmVhdCBhcyBhbiBvYmplY3QKICAgIGZvciBrLCB2IGluIHBhaXJzKHZhbCkgZG8KICAgICAgaWYgdHlwZShrKSB+PSAic3RyaW5nIiB0aGVuCiAgICAgICAgZXJyb3IoImludmFsaWQgdGFibGU6IG1peGVkIG9yIGludmFsaWQga2V5IHR5cGVzIikKICAgICAgZW5kCiAgICAgIHRhYmxlLmluc2VydChyZXMsIGVuY29kZShrLCBzdGFjaykgLi4gIjoiIC4uIGVuY29kZSh2LCBzdGFjaykpCiAgICBlbmQKICAgIHN0YWNrW3ZhbF0gPSBuaWwKICAgIHJldHVybiAieyIgLi4gdGFibGUuY29uY2F0KHJlcywgIiwiKSAuLiAifSIKICBlbmQKZW5kCgoKbG9jYWwgZnVuY3Rpb24gZW5jb2RlX3N0cmluZyh2YWwpCiAgcmV0dXJuICciJyAuLiB2YWw6Z3N1YignWyV6XDEtXDMxXFwiXScsIGVzY2FwZV9jaGFyKSAuLiAnIicKZW5kCgoKbG9jYWwgZnVuY3Rpb24gZW5jb2RlX251bWJlcih2YWwpCiAgLS0gQ2hlY2sgZm9yIE5hTiwgLWluZiBhbmQgaW5mCiAgaWYgdmFsIH49IHZhbCBvciB2YWwgPD0gLW1hdGguaHVnZSBvciB2YWwgPj0gbWF0aC5odWdlIHRoZW4KICAgIGVycm9yKCJ1bmV4cGVjdGVkIG51bWJlciB2YWx1ZSAnIiAuLiB0b3N0cmluZyh2YWwpIC4uICInIikKICBlbmQKICByZXR1cm4gc3RyaW5nLmZvcm1hdCgiJS4xNGciLCB2YWwpCmVuZAoKCmxvY2FsIHR5cGVfZnVuY19tYXAgPSB7CiAgWyAibmlsIiAgICAgXSA9IGVuY29kZV9uaWwsCiAgWyAidGFibGUiICAgXSA9IGVuY29kZV90YWJsZSwKICBbICJzdHJpbmciICBdID0gZW5jb2RlX3N0cmluZywKICBbICJudW1iZXIiICBdID0gZW5jb2RlX251bWJlciwKICBbICJib29sZWFuIiBdID0gdG9zdHJpbmcsCn0KCgplbmNvZGUgPSBmdW5jdGlvbih2YWwsIHN0YWNrKQogIGxvY2FsIHQgPSB0eXBlKHZhbCkKICBsb2NhbCBmID0gdHlwZV9mdW5jX21hcFt0XQogIGlmIGYgdGhlbgogICAgcmV0dXJuIGYodmFsLCBzdGFjaykKICBlbmQKICBlcnJvcigidW5leHBlY3RlZCB0eXBlICciIC4uIHQgLi4gIiciKQplbmQKCgpmdW5jdGlvbiBjanNvbi5lbmNvZGUodmFsKQogIHJldHVybiAoIGVuY29kZSh2YWwpICkKZW5kCgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQotLSBEZWNvZGUKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKbG9jYWwgcGFyc2UKCmxvY2FsIGZ1bmN0aW9uIGNyZWF0ZV9zZXQoLi4uKQogIGxvY2FsIHJlcyA9IHt9CiAgZm9yIGkgPSAxLCBzZWxlY3QoIiMiLCAuLi4pIGRvCiAgICByZXNbIHNlbGVjdChpLCAuLi4pIF0gPSB0cnVlCiAgZW5kCiAgcmV0dXJuIHJlcwplbmQKCmxvY2FsIHNwYWNlX2NoYXJzICAgPSBjcmVhdGVfc2V0KCIgIiwgIlx0IiwgIlxyIiwgIlxuIikKbG9jYWwgZGVsaW1fY2hhcnMgICA9IGNyZWF0ZV9zZXQoIiAiLCAiXHQiLCAiXHIiLCAiXG4iLCAiXSIsICJ9IiwgIiwiKQpsb2NhbCBlc2NhcGVfY2hhcnMgID0gY3JlYXRlX3NldCgiXFwiLCAiLyIsICciJywgImIiLCAiZiIsICJuIiwgInIiLCAidCIsICJ1IikKbG9jYWwgbGl0ZXJhbHMgICAgICA9IGNyZWF0ZV9zZXQoInRydWUiLCAiZmFsc2UiLCAibnVsbCIpCgpsb2NhbCBsaXRlcmFsX21hcCA9IHsKICBbICJ0cnVlIiAgXSA9IHRydWUsCiAgWyAiZmFsc2UiIF0gPSBmYWxzZSwKICBbICJudWxsIiAgXSA9IG5pbCwKfQoKCmxvY2FsIGZ1bmN0aW9uIG5leHRfY2hhcihzdHIsIGlkeCwgc2V0LCBuZWdhdGUpCiAgZm9yIGkgPSBpZHgsICNzdHIgZG8KICAgIGlmIHNldFtzdHI6c3ViKGksIGkpXSB+PSBuZWdhdGUgdGhlbgogICAgICByZXR1cm4gaQogICAgZW5kCiAgZW5kCiAgcmV0dXJuICNzdHIgKyAxCmVuZAoKCmxvY2FsIGZ1bmN0aW9uIGRlY29kZV9lcnJvcihzdHIsIGlkeCwgbXNnKQogIGxvY2FsIGxpbmVfY291bnQgPSAxCiAgbG9jYWwgY29sX2NvdW50ID0gMQogIGZvciBpID0gMSwgaWR4IC0gMSBkbwogICAgY29sX2NvdW50ID0gY29sX2NvdW50ICsgMQogICAgaWYgc3RyOnN1YihpLCBpKSA9PSAiXG4iIHRoZW4KICAgICAgbGluZV9jb3VudCA9IGxpbmVfY291bnQgKyAxCiAgICAgIGNvbF9jb3VudCA9IDEKICAgIGVuZAogIGVuZAogIGVycm9yKCBzdHJpbmcuZm9ybWF0KCIlcyBhdCBsaW5lICVkIGNvbCAlZCIsIG1zZywgbGluZV9jb3VudCwgY29sX2NvdW50KSApCmVuZAoKCmxvY2FsIGZ1bmN0aW9uIGNvZGVwb2ludF90b191dGY4KG4pCiAgLS0gaHR0cDovL3NjcmlwdHMuc2lsLm9yZy9jbXMvc2NyaXB0cy9wYWdlLnBocD9zaXRlX2lkPW5yc2kmaWQ9aXdzLWFwcGVuZGl4YQogIGxvY2FsIGYgPSBtYXRoLmZsb29yCiAgaWYgbiA8PSAweDdmIHRoZW4KICAgIHJldHVybiBzdHJpbmcuY2hhcihuKQogIGVsc2VpZiBuIDw9IDB4N2ZmIHRoZW4KICAgIHJldHVybiBzdHJpbmcuY2hhcihmKG4gLyA2NCkgKyAxOTIsIG4gJSA2NCArIDEyOCkKICBlbHNlaWYgbiA8PSAweGZmZmYgdGhlbgogICAgcmV0dXJuIHN0cmluZy5jaGFyKGYobiAvIDQwOTYpICsgMjI0LCBmKG4gJSA0MDk2IC8gNjQpICsgMTI4LCBuICUgNjQgKyAxMjgpCiAgZWxzZWlmIG4gPD0gMHgxMGZmZmYgdGhlbgogICAgcmV0dXJuIHN0cmluZy5jaGFyKGYobiAvIDI2MjE0NCkgKyAyNDAsIGYobiAlIDI2MjE0NCAvIDQwOTYpICsgMTI4LAogICAgICAgICAgICAgICAgICAgICAgIGYobiAlIDQwOTYgLyA2NCkgKyAxMjgsIG4gJSA2NCArIDEyOCkKICBlbmQKICBlcnJvciggc3RyaW5nLmZvcm1hdCgiaW52YWxpZCB1bmljb2RlIGNvZGVwb2ludCAnJXgnIiwgbikgKQplbmQKCgpsb2NhbCBmdW5jdGlvbiBwYXJzZV91bmljb2RlX2VzY2FwZShzKQogIGxvY2FsIG4xID0gdG9udW1iZXIoIHM6c3ViKDMsIDYpLCAgMTYgKQogIGxvY2FsIG4yID0gdG9udW1iZXIoIHM6c3ViKDksIDEyKSwgMTYgKQogIC0tIFN1cnJvZ2F0ZSBwYWlyPwogIGlmIG4yIHRoZW4KICAgIHJldHVybiBjb2RlcG9pbnRfdG9fdXRmOCgobjEgLSAweGQ4MDApICogMHg0MDAgKyAobjIgLSAweGRjMDApICsgMHgxMDAwMCkKICBlbHNlCiAgICByZXR1cm4gY29kZXBvaW50X3RvX3V0ZjgobjEpCiAgZW5kCmVuZAoKCmxvY2FsIGZ1bmN0aW9uIHBhcnNlX3N0cmluZyhzdHIsIGkpCiAgbG9jYWwgaGFzX3VuaWNvZGVfZXNjYXBlID0gZmFsc2UKICBsb2NhbCBoYXNfc3Vycm9nYXRlX2VzY2FwZSA9IGZhbHNlCiAgbG9jYWwgaGFzX2VzY2FwZSA9IGZhbHNlCiAgbG9jYWwgbGFzdAogIGZvciBqID0gaSArIDEsICNzdHIgZG8KICAgIGxvY2FsIHggPSBzdHI6Ynl0ZShqKQoKICAgIGlmIHggPCAzMiB0aGVuCiAgICAgIGRlY29kZV9lcnJvcihzdHIsIGosICJjb250cm9sIGNoYXJhY3RlciBpbiBzdHJpbmciKQogICAgZW5kCgogICAgaWYgbGFzdCA9PSA5MiB0aGVuIC0tICJcXCIgKGVzY2FwZSBjaGFyKQogICAgICBpZiB4ID09IDExNyB0aGVuIC0tICJ1IiAodW5pY29kZSBlc2NhcGUgc2VxdWVuY2UpCiAgICAgICAgbG9jYWwgaGV4ID0gc3RyOnN1YihqICsgMSwgaiArIDUpCiAgICAgICAgaWYgbm90IGhleDpmaW5kKCIleCV4JXgleCIpIHRoZW4KICAgICAgICAgIGRlY29kZV9lcnJvcihzdHIsIGosICJpbnZhbGlkIHVuaWNvZGUgZXNjYXBlIGluIHN0cmluZyIpCiAgICAgICAgZW5kCiAgICAgICAgaWYgaGV4OmZpbmQoIl5bZERdWzg5YUFiQl0iKSB0aGVuCiAgICAgICAgICBoYXNfc3Vycm9nYXRlX2VzY2FwZSA9IHRydWUKICAgICAgICBlbHNlCiAgICAgICAgICBoYXNfdW5pY29kZV9lc2NhcGUgPSB0cnVlCiAgICAgICAgZW5kCiAgICAgIGVsc2UKICAgICAgICBsb2NhbCBjID0gc3RyaW5nLmNoYXIoeCkKICAgICAgICBpZiBub3QgZXNjYXBlX2NoYXJzW2NdIHRoZW4KICAgICAgICAgIGRlY29kZV9lcnJvcihzdHIsIGosICJpbnZhbGlkIGVzY2FwZSBjaGFyICciIC4uIGMgLi4gIicgaW4gc3RyaW5nIikKICAgICAgICBlbmQKICAgICAgICBoYXNfZXNjYXBlID0gdHJ1ZQogICAgICBlbmQKICAgICAgbGFzdCA9IG5pbAoKICAgIGVsc2VpZiB4ID09IDM0IHRoZW4gLS0gJyInIChlbmQgb2Ygc3RyaW5nKQogICAgICBsb2NhbCBzID0gc3RyOnN1YihpICsgMSwgaiAtIDEpCiAgICAgIGlmIGhhc19zdXJyb2dhdGVfZXNjYXBlIHRoZW4KICAgICAgICBzID0gczpnc3ViKCJcXHVbZERdWzg5YUFiQl0uLlxcdS4uLi4iLCBwYXJzZV91bmljb2RlX2VzY2FwZSkKICAgICAgZW5kCiAgICAgIGlmIGhhc191bmljb2RlX2VzY2FwZSB0aGVuCiAgICAgICAgcyA9IHM6Z3N1YigiXFx1Li4uLiIsIHBhcnNlX3VuaWNvZGVfZXNjYXBlKQogICAgICBlbmQKICAgICAgaWYgaGFzX2VzY2FwZSB0aGVuCiAgICAgICAgcyA9IHM6Z3N1YigiXFwuIiwgZXNjYXBlX2NoYXJfbWFwX2ludikKICAgICAgZW5kCiAgICAgIHJldHVybiBzLCBqICsgMQoKICAgIGVsc2UKICAgICAgbGFzdCA9IHgKICAgIGVuZAogIGVuZAogIGRlY29kZV9lcnJvcihzdHIsIGksICJleHBlY3RlZCBjbG9zaW5nIHF1b3RlIGZvciBzdHJpbmciKQplbmQKCgpsb2NhbCBmdW5jdGlvbiBwYXJzZV9udW1iZXIoc3RyLCBpKQogIGxvY2FsIHggPSBuZXh0X2NoYXIoc3RyLCBpLCBkZWxpbV9jaGFycykKICBsb2NhbCBzID0gc3RyOnN1YihpLCB4IC0gMSkKICBsb2NhbCBuID0gdG9udW1iZXIocykKICBpZiBub3QgbiB0aGVuCiAgICBkZWNvZGVfZXJyb3Ioc3RyLCBpLCAiaW52YWxpZCBudW1iZXIgJyIgLi4gcyAuLiAiJyIpCiAgZW5kCiAgcmV0dXJuIG4sIHgKZW5kCgoKbG9jYWwgZnVuY3Rpb24gcGFyc2VfbGl0ZXJhbChzdHIsIGkpCiAgbG9jYWwgeCA9IG5leHRfY2hhcihzdHIsIGksIGRlbGltX2NoYXJzKQogIGxvY2FsIHdvcmQgPSBzdHI6c3ViKGksIHggLSAxKQogIGlmIG5vdCBsaXRlcmFsc1t3b3JkXSB0aGVuCiAgICBkZWNvZGVfZXJyb3Ioc3RyLCBpLCAiaW52YWxpZCBsaXRlcmFsICciIC4uIHdvcmQgLi4gIiciKQogIGVuZAogIHJldHVybiBsaXRlcmFsX21hcFt3b3JkXSwgeAplbmQKCgpsb2NhbCBmdW5jdGlvbiBwYXJzZV9hcnJheShzdHIsIGkpCiAgbG9jYWwgcmVzID0ge30KICBsb2NhbCBuID0gMQogIGkgPSBpICsgMQogIHdoaWxlIDEgZG8KICAgIGxvY2FsIHgKICAgIGkgPSBuZXh0X2NoYXIoc3RyLCBpLCBzcGFjZV9jaGFycywgdHJ1ZSkKICAgIC0tIEVtcHR5IC8gZW5kIG9mIGFycmF5PwogICAgaWYgc3RyOnN1YihpLCBpKSA9PSAiXSIgdGhlbgogICAgICBpID0gaSArIDEKICAgICAgYnJlYWsKICAgIGVuZAogICAgLS0gUmVhZCB0b2tlbgogICAgeCwgaSA9IHBhcnNlKHN0ciwgaSkKICAgIHJlc1tuXSA9IHgKICAgIG4gPSBuICsgMQogICAgLS0gTmV4dCB0b2tlbgogICAgaSA9IG5leHRfY2hhcihzdHIsIGksIHNwYWNlX2NoYXJzLCB0cnVlKQogICAgbG9jYWwgY2hyID0gc3RyOnN1YihpLCBpKQogICAgaSA9IGkgKyAxCiAgICBpZiBjaHIgPT0gIl0iIHRoZW4gYnJlYWsgZW5kCiAgICBpZiBjaHIgfj0gIiwiIHRoZW4gZGVjb2RlX2Vycm9yKHN0ciwgaSwgImV4cGVjdGVkICddJyBvciAnLCciKSBlbmQKICBlbmQKICByZXR1cm4gcmVzLCBpCmVuZAoKCmxvY2FsIGZ1bmN0aW9uIHBhcnNlX29iamVjdChzdHIsIGkpCiAgbG9jYWwgcmVzID0ge30KICBpID0gaSArIDEKICB3aGlsZSAxIGRvCiAgICBsb2NhbCBrZXksIHZhbAogICAgaSA9IG5leHRfY2hhcihzdHIsIGksIHNwYWNlX2NoYXJzLCB0cnVlKQogICAgLS0gRW1wdHkgLyBlbmQgb2Ygb2JqZWN0PwogICAgaWYgc3RyOnN1YihpLCBpKSA9PSAifSIgdGhlbgogICAgICBpID0gaSArIDEKICAgICAgYnJlYWsKICAgIGVuZAogICAgLS0gUmVhZCBrZXkKICAgIGlmIHN0cjpzdWIoaSwgaSkgfj0gJyInIHRoZW4KICAgICAgZGVjb2RlX2Vycm9yKHN0ciwgaSwgImV4cGVjdGVkIHN0cmluZyBmb3Iga2V5IikKICAgIGVuZAogICAga2V5LCBpID0gcGFyc2Uoc3RyLCBpKQogICAgLS0gUmVhZCAnOicgZGVsaW1pdGVyCiAgICBpID0gbmV4dF9jaGFyKHN0ciwgaSwgc3BhY2VfY2hhcnMsIHRydWUpCiAgICBpZiBzdHI6c3ViKGksIGkpIH49ICI6IiB0aGVuCiAgICAgIGRlY29kZV9lcnJvcihzdHIsIGksICJleHBlY3RlZCAnOicgYWZ0ZXIga2V5IikKICAgIGVuZAogICAgaSA9IG5leHRfY2hhcihzdHIsIGkgKyAxLCBzcGFjZV9jaGFycywgdHJ1ZSkKICAgIC0tIFJlYWQgdmFsdWUKICAgIHZhbCwgaSA9IHBhcnNlKHN0ciwgaSkKICAgIC0tIFNldAogICAgcmVzW2tleV0gPSB2YWwKICAgIC0tIE5leHQgdG9rZW4KICAgIGkgPSBuZXh0X2NoYXIoc3RyLCBpLCBzcGFjZV9jaGFycywgdHJ1ZSkKICAgIGxvY2FsIGNociA9IHN0cjpzdWIoaSwgaSkKICAgIGkgPSBpICsgMQogICAgaWYgY2hyID09ICJ9IiB0aGVuIGJyZWFrIGVuZAogICAgaWYgY2hyIH49ICIsIiB0aGVuIGRlY29kZV9lcnJvcihzdHIsIGksICJleHBlY3RlZCAnfScgb3IgJywnIikgZW5kCiAgZW5kCiAgcmV0dXJuIHJlcywgaQplbmQKCgpsb2NhbCBjaGFyX2Z1bmNfbWFwID0gewogIFsgJyInIF0gPSBwYXJzZV9zdHJpbmcsCiAgWyAiMCIgXSA9IHBhcnNlX251bWJlciwKICBbICIxIiBdID0gcGFyc2VfbnVtYmVyLAogIFsgIjIiIF0gPSBwYXJzZV9udW1iZXIsCiAgWyAiMyIgXSA9IHBhcnNlX251bWJlciwKICBbICI0IiBdID0gcGFyc2VfbnVtYmVyLAogIFsgIjUiIF0gPSBwYXJzZV9udW1iZXIsCiAgWyAiNiIgXSA9IHBhcnNlX251bWJlciwKICBbICI3IiBdID0gcGFyc2VfbnVtYmVyLAogIFsgIjgiIF0gPSBwYXJzZV9udW1iZXIsCiAgWyAiOSIgXSA9IHBhcnNlX251bWJlciwKICBbICItIiBdID0gcGFyc2VfbnVtYmVyLAogIFsgInQiIF0gPSBwYXJzZV9saXRlcmFsLAogIFsgImYiIF0gPSBwYXJzZV9saXRlcmFsLAogIFsgIm4iIF0gPSBwYXJzZV9saXRlcmFsLAogIFsgIlsiIF0gPSBwYXJzZV9hcnJheSwKICBbICJ7IiBdID0gcGFyc2Vfb2JqZWN0LAp9CgoKcGFyc2UgPSBmdW5jdGlvbihzdHIsIGlkeCkKICBsb2NhbCBjaHIgPSBzdHI6c3ViKGlkeCwgaWR4KQogIGxvY2FsIGYgPSBjaGFyX2Z1bmNfbWFwW2Nocl0KICBpZiBmIHRoZW4KICAgIHJldHVybiBmKHN0ciwgaWR4KQogIGVuZAogIGRlY29kZV9lcnJvcihzdHIsIGlkeCwgInVuZXhwZWN0ZWQgY2hhcmFjdGVyICciIC4uIGNociAuLiAiJyIpCmVuZAoKCmZ1bmN0aW9uIGNqc29uLmRlY29kZShzdHIpCiAgaWYgdHlwZShzdHIpIH49ICJzdHJpbmciIHRoZW4KICAgIGVycm9yKCJleHBlY3RlZCBhcmd1bWVudCBvZiB0eXBlIHN0cmluZywgZ290ICIgLi4gdHlwZShzdHIpKQogIGVuZAogIGxvY2FsIHJlcywgaWR4ID0gcGFyc2Uoc3RyLCBuZXh0X2NoYXIoc3RyLCAxLCBzcGFjZV9jaGFycywgdHJ1ZSkpCiAgaWR4ID0gbmV4dF9jaGFyKHN0ciwgaWR4LCBzcGFjZV9jaGFycywgdHJ1ZSkKICBpZiBpZHggPD0gI3N0ciB0aGVuCiAgICBkZWNvZGVfZXJyb3Ioc3RyLCBpZHgsICJ0cmFpbGluZyBnYXJiYWdlIikKICBlbmQKICByZXR1cm4gcmVzCmVuZApyZXR1cm4gY2pzb24="
BIT_LUA = "LS1bWwoKTFVBIE1PRFVMRQoKICBiaXQubnVtYmVybHVhIC0gQml0d2lzZSBvcGVyYXRpb25zIGltcGxlbWVudGVkIGluIHB1cmUgTHVhIGFzIG51bWJlcnMsCiAgICB3aXRoIEx1YSA1LjIgJ2JpdDMyJyBhbmQgKEx1YUpJVCkgTHVhQml0T3AgJ2JpdCcgY29tcGF0aWJpbGl0eSBpbnRlcmZhY2VzLgoKU1lOT1BTSVMKCiAgbG9jYWwgYml0ID0gcmVxdWlyZSAnYml0Lm51bWJlcmx1YScKICBwcmludChiaXQuYmFuZCgweGZmMDBmZjAwLCAweDAwZmYwMGZmKSkgLS0+IDB4ZmZmZmZmZmYKICAKICAtLSBJbnRlcmZhY2UgcHJvdmlkaW5nIHN0cm9uZyBMdWEgNS4yICdiaXQzMicgY29tcGF0aWJpbGl0eQogIGxvY2FsIGJpdDMyID0gcmVxdWlyZSAnYml0Lm51bWJlcmx1YScuYml0MzIKICBhc3NlcnQoYml0MzIuYmFuZCgtMSkgPT0gMHhmZmZmZmZmZikKICAKICAtLSBJbnRlcmZhY2UgcHJvdmlkaW5nIHN0cm9uZyAoTHVhSklUKSBMdWFCaXRPcCAnYml0JyBjb21wYXRpYmlsaXR5CiAgbG9jYWwgYml0ID0gcmVxdWlyZSAnYml0Lm51bWJlcmx1YScuYml0CiAgYXNzZXJ0KGJpdC50b2JpdCgweGZmZmZmZmZmKSA9PSAtMSkKICAKREVTQ1JJUFRJT04KICAKICBUaGlzIGxpYnJhcnkgaW1wbGVtZW50cyBiaXR3aXNlIG9wZXJhdGlvbnMgZW50aXJlbHkgaW4gTHVhLgogIFRoaXMgbW9kdWxlIGlzIHR5cGljYWxseSBpbnRlbmRlZCBpZiBmb3Igc29tZSByZWFzb25zIHlvdSBkb24ndCB3YW50CiAgdG8gb3IgY2Fubm90ICBpbnN0YWxsIGEgcG9wdWxhciBDIGJhc2VkIGJpdCBsaWJyYXJ5IGxpa2UgQml0T3AgJ2JpdCcgWzFdCiAgKHdoaWNoIGNvbWVzIHByZS1pbnN0YWxsZWQgd2l0aCBMdWFKSVQpIG9yICdiaXQzMicgKHdoaWNoIGNvbWVzCiAgcHJlLWluc3RhbGxlZCB3aXRoIEx1YSA1LjIpIGJ1dCB3YW50IGEgc2ltaWxhciBpbnRlcmZhY2UuCiAgCiAgVGhpcyBtb2R1bGVzIHJlcHJlc2VudHMgYml0IGFycmF5cyBhcyBub24tbmVnYXRpdmUgTHVhIG51bWJlcnMuIFsxXQogIEl0IGNhbiByZXByZXNlbnQgMzItYml0IGJpdCBhcnJheXMgd2hlbiBMdWEgaXMgY29tcGlsZWQKICB3aXRoIGx1YV9OdW1iZXIgYXMgZG91YmxlLXByZWNpc2lvbiBJRUVFIDc1NCBmbG9hdGluZyBwb2ludC4KCiAgVGhlIG1vZHVsZSBpcyBuZWFybHkgdGhlIG1vc3QgZWZmaWNpZW50IGl0IGNhbiBiZSBidXQgbWF5IGJlIGEgZmV3IHRpbWVzCiAgc2xvd2VyIHRoYW4gdGhlIEMgYmFzZWQgYml0IGxpYnJhcmllcyBhbmQgaXMgb3JkZXJzIG9yIG1hZ25pdHVkZQogIHNsb3dlciB0aGFuIEx1YUpJVCBiaXQgb3BlcmF0aW9ucywgd2hpY2ggY29tcGlsZSB0byBuYXRpdmUgY29kZS4gIFRoZXJlZm9yZSwKICB0aGlzIGxpYnJhcnkgaXMgaW5mZXJpb3IgaW4gcGVyZm9ybWFuZSB0byB0aGUgb3RoZXIgbW9kdWxlcy4KCiAgVGhlIGB4b3JgIGZ1bmN0aW9uIGluIHRoaXMgbW9kdWxlIGlzIGJhc2VkIHBhcnRseSBvbiBSb2JlcnRvIEllcnVzYWxpbXNjaHkncwogIHBvc3QgaW4gaHR0cDovL2x1YS11c2Vycy5vcmcvbGlzdHMvbHVhLWwvMjAwMi0wOS9tc2cwMDEzNC5odG1sIC4KICAKICBUaGUgaW5jbHVkZWQgQklULmJpdDMyIGFuZCBCSVQuYml0IHN1YmxpYnJhcmllcyBhaW1zIHRvIHByb3ZpZGUgMTAwJQogIGNvbXBhdGliaWxpdHkgd2l0aCB0aGUgTHVhIDUuMiAiYml0MzIiIGFuZCAoTHVhSklUKSBMdWFCaXRPcCAiYml0IiBsaWJyYXJ5LgogIFRoaXMgY29tcGF0YmlsaXR5IGlzIGF0IHRoZSBjb3N0IG9mIHNvbWUgZWZmaWNpZW5jeSBzaW5jZSBpbnB1dHRlZAogIG51bWJlcnMgYXJlIG5vcm1hbGl6ZWQgYW5kIG1vcmUgZ2VuZXJhbCBmb3JtcyAoZS5nLiBtdWx0aS1hcmd1bWVudAogIGJpdHdpc2Ugb3BlcmF0b3JzKSBhcmUgc3VwcG9ydGVkLgogIApTVEFUVVMKCiAgV0FSTklORzogTm90IGFsbCBjb3JuZXIgY2FzZXMgaGF2ZSBiZWVuIHRlc3RlZCBhbmQgZG9jdW1lbnRlZC4KICBTb21lIGF0dGVtcHQgd2FzIG1hZGUgdG8gbWFrZSB0aGVzZSBzaW1pbGFyIHRvIHRoZSBMdWEgNS4yIFsyXQogIGFuZCBMdWFKaXQgQml0T3AgWzNdIGxpYnJhcmllcywgYnV0IHRoaXMgaXMgbm90IGZ1bGx5IHRlc3RlZCBhbmQgdGhlcmUKICBhcmUgY3VycmVudGx5IHNvbWUgZGlmZmVyZW5jZXMuICBBZGRyZXNzaW5nIHRoZXNlIGRpZmZlcmVuY2VzIG1heQogIGJlIGltcHJvdmVkIGluIHRoZSBmdXR1cmUgYnV0IGl0IGlzIG5vdCB5ZXQgZnVsbHkgZGV0ZXJtaW5lZCBob3cgdG8KICByZXNvbHZlIHRoZXNlIGRpZmZlcmVuY2VzLgogIAogIFRoZSBCSVQuYml0MzIgbGlicmFyeSBwYXNzZXMgdGhlIEx1YSA1LjIgdGVzdCBzdWl0ZSAoYml0d2lzZS5sdWEpCiAgaHR0cDovL3d3dy5sdWEub3JnL3Rlc3RzLzUuMi8gLiAgVGhlIEJJVC5iaXQgbGlicmFyeSBwYXNzZXMgdGhlIEx1YUJpdE9wCiAgdGVzdCBzdWl0ZSAoYml0dGVzdC5sdWEpLiAgSG93ZXZlciwgdGhlc2UgaGF2ZSBub3QgYmVlbiB0ZXN0ZWQgb24KICBwbGF0Zm9ybXMgd2l0aCBMdWEgY29tcGlsZWQgd2l0aCAzMi1iaXQgaW50ZWdlciBudW1iZXJzLgoKQVBJCgogIEJJVC50b2JpdCh4KSAtLT4gegogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBCaXRPcC4KICAgIAogIEJJVC50b2hleCh4LCBuKQogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBCaXRPcC4KICAKICBCSVQuYmFuZCh4LCB5KSAtLT4gegogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBMdWEgNS4yIGFuZCBCaXRPcCBidXQgcmVxdWlyZXMgdHdvIGFyZ3VtZW50cy4KICAKICBCSVQuYm9yKHgsIHkpIC0tPiB6CiAgCiAgICBTaW1pbGFyIHRvIGZ1bmN0aW9uIGluIEx1YSA1LjIgYW5kIEJpdE9wIGJ1dCByZXF1aXJlcyB0d28gYXJndW1lbnRzLgoKICBCSVQuYnhvcih4LCB5KSAtLT4gegogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBMdWEgNS4yIGFuZCBCaXRPcCBidXQgcmVxdWlyZXMgdHdvIGFyZ3VtZW50cy4KICAKICBCSVQuYm5vdCh4KSAtLT4gegogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBMdWEgNS4yIGFuZCBCaXRPcC4KCiAgQklULmxzaGlmdCh4LCBkaXNwKSAtLT4gegogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBMdWEgNS4yICh3YXJuaW5nOiBCaXRPcCB1c2VzIHVuc2lnbmVkIGxvd2VyIDUgYml0cyBvZiBzaGlmdCksCiAgCiAgQklULnJzaGlmdCh4LCBkaXNwKSAtLT4gegogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBMdWEgNS4yICh3YXJuaW5nOiBCaXRPcCB1c2VzIHVuc2lnbmVkIGxvd2VyIDUgYml0cyBvZiBzaGlmdCksCgogIEJJVC5leHRyYWN0KHgsIGZpZWxkIFssIHdpZHRoXSkgLS0+IHoKICAKICAgIFNpbWlsYXIgdG8gZnVuY3Rpb24gaW4gTHVhIDUuMi4KICAKICBCSVQucmVwbGFjZSh4LCB2LCBmaWVsZCwgd2lkdGgpIC0tPiB6CiAgCiAgICBTaW1pbGFyIHRvIGZ1bmN0aW9uIGluIEx1YSA1LjIuCiAgCiAgQklULmJzd2FwKHgpIC0tPiB6CiAgCiAgICBTaW1pbGFyIHRvIGZ1bmN0aW9uIGluIEx1YSA1LjIuCgogIEJJVC5ycm90YXRlKHgsIGRpc3ApIC0tPiB6CiAgQklULnJvcih4LCBkaXNwKSAtLT4gegogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBMdWEgNS4yIGFuZCBCaXRPcC4KCiAgQklULmxyb3RhdGUoeCwgZGlzcCkgLS0+IHoKICBCSVQucm9sKHgsIGRpc3ApIC0tPiB6CgogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBMdWEgNS4yIGFuZCBCaXRPcC4KICAKICBCSVQuYXJzaGlmdAogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBMdWEgNS4yIGFuZCBCaXRPcC4KICAgIAogIEJJVC5idGVzdAogIAogICAgU2ltaWxhciB0byBmdW5jdGlvbiBpbiBMdWEgNS4yIHdpdGggcmVxdWlyZXMgdHdvIGFyZ3VtZW50cy4KCiAgQklULmJpdDMyCiAgCiAgICBUaGlzIHRhYmxlIGNvbnRhaW5zIGZ1bmN0aW9ucyB0aGF0IGFpbSB0byBwcm92aWRlIDEwMCUgY29tcGF0aWJpbGl0eQogICAgd2l0aCB0aGUgTHVhIDUuMiAiYml0MzIiIGxpYnJhcnkuCiAgICAKICAgIGJpdDMyLmFyc2hpZnQgKHgsIGRpc3ApIC0tPiB6CiAgICBiaXQzMi5iYW5kICguLi4pIC0tPiB6CiAgICBiaXQzMi5ibm90ICh4KSAtLT4gegogICAgYml0MzIuYm9yICguLi4pIC0tPiB6CiAgICBiaXQzMi5idGVzdCAoLi4uKSAtLT4gdHJ1ZSB8IGZhbHNlCiAgICBiaXQzMi5ieG9yICguLi4pIC0tPiB6CiAgICBiaXQzMi5leHRyYWN0ICh4LCBmaWVsZCBbLCB3aWR0aF0pIC0tPiB6CiAgICBiaXQzMi5yZXBsYWNlICh4LCB2LCBmaWVsZCBbLCB3aWR0aF0pIC0tPiB6CiAgICBiaXQzMi5scm90YXRlICh4LCBkaXNwKSAtLT4gegogICAgYml0MzIubHNoaWZ0ICh4LCBkaXNwKSAtLT4gegogICAgYml0MzIucnJvdGF0ZSAoeCwgZGlzcCkgLS0+IHoKICAgIGJpdDMyLnJzaGlmdCAoeCwgZGlzcCkgLS0+IHoKCiAgQklULmJpdAogIAogICAgVGhpcyB0YWJsZSBjb250YWlucyBmdW5jdGlvbnMgdGhhdCBhaW0gdG8gcHJvdmlkZSAxMDAlIGNvbXBhdGliaWxpdHkKICAgIHdpdGggdGhlIEx1YUJpdE9wICJiaXQiIGxpYnJhcnkgKGZyb20gTHVhSklUKS4KICAgIAogICAgYml0LnRvYml0KHgpIC0tPiB5CiAgICBiaXQudG9oZXgoeCBbLG5dKSAtLT4geQogICAgYml0LmJub3QoeCkgLS0+IHkKICAgIGJpdC5ib3IoeDEgWyx4Mi4uLl0pIC0tPiB5CiAgICBiaXQuYmFuZCh4MSBbLHgyLi4uXSkgLS0+IHkKICAgIGJpdC5ieG9yKHgxIFsseDIuLi5dKSAtLT4geQogICAgYml0LmxzaGlmdCh4LCBuKSAtLT4geQogICAgYml0LnJzaGlmdCh4LCBuKSAtLT4geQogICAgYml0LmFyc2hpZnQoeCwgbikgLS0+IHkKICAgIGJpdC5yb2woeCwgbikgLS0+IHkKICAgIGJpdC5yb3IoeCwgbikgLS0+IHkKICAgIGJpdC5ic3dhcCh4KSAtLT4geQogICAgCkRFUEVOREVOQ0lFUwoKICBOb25lIChvdGhlciB0aGFuIEx1YSA1LjEgb3IgNS4yKS4KICAgIApET1dOTE9BRC9JTlNUQUxMQVRJT04KCiAgSWYgdXNpbmcgTHVhUm9ja3M6CiAgICBsdWFyb2NrcyBpbnN0YWxsIGx1YS1iaXQtbnVtYmVybHVhCgogIE90aGVyd2lzZSwgZG93bmxvYWQgPGh0dHBzOi8vZ2l0aHViLmNvbS9kYXZpZG0vbHVhLWJpdC1udW1iZXJsdWEvemlwYmFsbC9tYXN0ZXI+LgogIEFsdGVybmF0ZWx5LCBpZiB1c2luZyBnaXQ6CiAgICBnaXQgY2xvbmUgZ2l0Oi8vZ2l0aHViLmNvbS9kYXZpZG0vbHVhLWJpdC1udW1iZXJsdWEuZ2l0CiAgICBjZCBsdWEtYml0LW51bWJlcmx1YQogIE9wdGlvbmFsbHkgdW5wYWNrOgogICAgLi91dGlsLm1rCiAgb3IgdW5wYWNrIGFuZCBpbnN0YWxsIGluIEx1YVJvY2tzOgogICAgLi91dGlsLm1rIGluc3RhbGwgCgpSRUZFUkVOQ0VTCgogIFsxXSBodHRwOi8vbHVhLXVzZXJzLm9yZy93aWtpL0Zsb2F0aW5nUG9pbnQKICBbMl0gaHR0cDovL3d3dy5sdWEub3JnL21hbnVhbC81LjIvCiAgWzNdIGh0dHA6Ly9iaXRvcC5sdWFqaXQub3JnLwogIApMSUNFTlNFCgogIChjKSAyMDA4LTIwMTEgRGF2aWQgTWFudXJhLiAgTGljZW5zZWQgdW5kZXIgdGhlIHNhbWUgdGVybXMgYXMgTHVhIChNSVQpLgoKICBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5CiAgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKICBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCiAgdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAogIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwogIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgogIFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCiAgYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgogIFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCiAgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCiAgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gIElOIE5PIEVWRU5UIFNIQUxMIFRIRQogIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKICBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAogIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KICBUSEUgU09GVFdBUkUuCiAgKGVuZCBsaWNlbnNlKQoKLS1dXQoKbG9jYWwgTSA9IHtfVFlQRT0nbW9kdWxlJywgX05BTUU9J2JpdC5udW1iZXJsdWEnLCBfVkVSU0lPTj0nMC4zLjEuMjAxMjAxMzEnfQoKbG9jYWwgZmxvb3IgPSBtYXRoLmZsb29yCgpsb2NhbCBNT0QgPSAyXjMyCmxvY2FsIE1PRE0gPSBNT0QtMQoKbG9jYWwgZnVuY3Rpb24gbWVtb2l6ZShmKQogIGxvY2FsIG10ID0ge30KICBsb2NhbCB0ID0gc2V0bWV0YXRhYmxlKHt9LCBtdCkKICBmdW5jdGlvbiBtdDpfX2luZGV4KGspCiAgICBsb2NhbCB2ID0gZihrKTsgdFtrXSA9IHYKICAgIHJldHVybiB2CiAgZW5kCiAgcmV0dXJuIHQKZW5kCgpsb2NhbCBmdW5jdGlvbiBtYWtlX2JpdG9wX3VuY2FjaGVkKHQsIG0pCiAgbG9jYWwgZnVuY3Rpb24gYml0b3AoYSwgYikKICAgIGxvY2FsIHJlcyxwID0gMCwxCiAgICB3aGlsZSBhIH49IDAgYW5kIGIgfj0gMCBkbwogICAgICBsb2NhbCBhbSwgYm0gPSBhJW0sIGIlbQogICAgICByZXMgPSByZXMgKyB0W2FtXVtibV0qcAogICAgICBhID0gKGEgLSBhbSkgLyBtCiAgICAgIGIgPSAoYiAtIGJtKSAvIG0KICAgICAgcCA9IHAqbQogICAgZW5kCiAgICByZXMgPSByZXMgKyAoYStiKSpwCiAgICByZXR1cm4gcmVzCiAgZW5kCiAgcmV0dXJuIGJpdG9wCmVuZAoKbG9jYWwgZnVuY3Rpb24gbWFrZV9iaXRvcCh0KQogIGxvY2FsIG9wMSA9IG1ha2VfYml0b3BfdW5jYWNoZWQodCwyXjEpCiAgbG9jYWwgb3AyID0gbWVtb2l6ZShmdW5jdGlvbihhKQogICAgcmV0dXJuIG1lbW9pemUoZnVuY3Rpb24oYikKICAgICAgcmV0dXJuIG9wMShhLCBiKQogICAgZW5kKQogIGVuZCkKICByZXR1cm4gbWFrZV9iaXRvcF91bmNhY2hlZChvcDIsIDJeKHQubiBvciAxKSkKZW5kCgotLSBvaz8gIHByb2JhYmx5IG5vdCBpZiBydW5uaW5nIG9uIGEgMzItYml0IGludCBMdWEgbnVtYmVyIHR5cGUgcGxhdGZvcm0KZnVuY3Rpb24gTS50b2JpdCh4KQogIHJldHVybiB4ICUgMl4zMgplbmQKCk0uYnhvciA9IG1ha2VfYml0b3Age1swXT17WzBdPTAsWzFdPTF9LFsxXT17WzBdPTEsWzFdPTB9LCBuPTR9CmxvY2FsIGJ4b3IgPSBNLmJ4b3IKCmZ1bmN0aW9uIE0uYm5vdChhKSAgIHJldHVybiBNT0RNIC0gYSBlbmQKbG9jYWwgYm5vdCA9IE0uYm5vdAoKZnVuY3Rpb24gTS5iYW5kKGEsYikgcmV0dXJuICgoYStiKSAtIGJ4b3IoYSxiKSkvMiBlbmQKbG9jYWwgYmFuZCA9IE0uYmFuZAoKZnVuY3Rpb24gTS5ib3IoYSxiKSAgcmV0dXJuIE1PRE0gLSBiYW5kKE1PRE0gLSBhLCBNT0RNIC0gYikgZW5kCmxvY2FsIGJvciA9IE0uYm9yCgpsb2NhbCBsc2hpZnQsIHJzaGlmdCAtLSBmb3J3YXJkIGRlY2xhcmUKCmZ1bmN0aW9uIE0ucnNoaWZ0KGEsZGlzcCkgLS0gTHVhNS4yIGluc2lwcmVkCiAgaWYgZGlzcCA8IDAgdGhlbiByZXR1cm4gbHNoaWZ0KGEsLWRpc3ApIGVuZAogIHJldHVybiBmbG9vcihhICUgMl4zMiAvIDJeZGlzcCkKZW5kCnJzaGlmdCA9IE0ucnNoaWZ0CgpmdW5jdGlvbiBNLmxzaGlmdChhLGRpc3ApIC0tIEx1YTUuMiBpbnNwaXJlZAogIGlmIGRpc3AgPCAwIHRoZW4gcmV0dXJuIHJzaGlmdChhLC1kaXNwKSBlbmQgCiAgcmV0dXJuIChhICogMl5kaXNwKSAlIDJeMzIKZW5kCmxzaGlmdCA9IE0ubHNoaWZ0CgpmdW5jdGlvbiBNLnRvaGV4KHgsIG4pIC0tIEJpdE9wIHN0eWxlCiAgbiA9IG4gb3IgOAogIGxvY2FsIHVwCiAgaWYgbiA8PSAwIHRoZW4KICAgIGlmIG4gPT0gMCB0aGVuIHJldHVybiAnJyBlbmQKICAgIHVwID0gdHJ1ZQogICAgbiA9IC0gbgogIGVuZAogIHggPSBiYW5kKHgsIDE2Xm4tMSkKICByZXR1cm4gKCclMCcuLm4uLih1cCBhbmQgJ1gnIG9yICd4JykpOmZvcm1hdCh4KQplbmQKbG9jYWwgdG9oZXggPSBNLnRvaGV4CgpmdW5jdGlvbiBNLmV4dHJhY3QobiwgZmllbGQsIHdpZHRoKSAtLSBMdWE1LjIgaW5zcGlyZWQKICB3aWR0aCA9IHdpZHRoIG9yIDEKICByZXR1cm4gYmFuZChyc2hpZnQobiwgZmllbGQpLCAyXndpZHRoLTEpCmVuZApsb2NhbCBleHRyYWN0ID0gTS5leHRyYWN0CgpmdW5jdGlvbiBNLnJlcGxhY2UobiwgdiwgZmllbGQsIHdpZHRoKSAtLSBMdWE1LjIgaW5zcGlyZWQKICB3aWR0aCA9IHdpZHRoIG9yIDEKICBsb2NhbCBtYXNrMSA9IDJed2lkdGgtMQogIHYgPSBiYW5kKHYsIG1hc2sxKSAtLSByZXF1aXJlZCBieSBzcGVjPwogIGxvY2FsIG1hc2sgPSBibm90KGxzaGlmdChtYXNrMSwgZmllbGQpKQogIHJldHVybiBiYW5kKG4sIG1hc2spICsgbHNoaWZ0KHYsIGZpZWxkKQplbmQKbG9jYWwgcmVwbGFjZSA9IE0ucmVwbGFjZQoKZnVuY3Rpb24gTS5ic3dhcCh4KSAgLS0gQml0T3Agc3R5bGUKICBsb2NhbCBhID0gYmFuZCh4LCAweGZmKTsgeCA9IHJzaGlmdCh4LCA4KQogIGxvY2FsIGIgPSBiYW5kKHgsIDB4ZmYpOyB4ID0gcnNoaWZ0KHgsIDgpCiAgbG9jYWwgYyA9IGJhbmQoeCwgMHhmZik7IHggPSByc2hpZnQoeCwgOCkKICBsb2NhbCBkID0gYmFuZCh4LCAweGZmKQogIHJldHVybiBsc2hpZnQobHNoaWZ0KGxzaGlmdChhLCA4KSArIGIsIDgpICsgYywgOCkgKyBkCmVuZApsb2NhbCBic3dhcCA9IE0uYnN3YXAKCmZ1bmN0aW9uIE0ucnJvdGF0ZSh4LCBkaXNwKSAgLS0gTHVhNS4yIGluc3BpcmVkCiAgZGlzcCA9IGRpc3AgJSAzMgogIGxvY2FsIGxvdyA9IGJhbmQoeCwgMl5kaXNwLTEpCiAgcmV0dXJuIHJzaGlmdCh4LCBkaXNwKSArIGxzaGlmdChsb3csIDMyLWRpc3ApCmVuZApsb2NhbCBycm90YXRlID0gTS5ycm90YXRlCgpmdW5jdGlvbiBNLmxyb3RhdGUoeCwgZGlzcCkgIC0tIEx1YTUuMiBpbnNwaXJlZAogIHJldHVybiBycm90YXRlKHgsIC1kaXNwKQplbmQKbG9jYWwgbHJvdGF0ZSA9IE0ubHJvdGF0ZQoKTS5yb2wgPSBNLmxyb3RhdGUgIC0tIEx1YU9wIGluc3BpcmVkCk0ucm9yID0gTS5ycm90YXRlICAtLSBMdWFPcCBpbnNpcHJlZAoKCmZ1bmN0aW9uIE0uYXJzaGlmdCh4LCBkaXNwKSAtLSBMdWE1LjIgaW5zcGlyZWQKICBsb2NhbCB6ID0gcnNoaWZ0KHgsIGRpc3ApCiAgaWYgeCA+PSAweDgwMDAwMDAwIHRoZW4geiA9IHogKyBsc2hpZnQoMl5kaXNwLTEsIDMyLWRpc3ApIGVuZAogIHJldHVybiB6CmVuZApsb2NhbCBhcnNoaWZ0ID0gTS5hcnNoaWZ0CgpmdW5jdGlvbiBNLmJ0ZXN0KHgsIHkpIC0tIEx1YTUuMiBpbnNwaXJlZAogIHJldHVybiBiYW5kKHgsIHkpIH49IDAKZW5kCgotLQotLSBTdGFydCBMdWEgNS4yICJiaXQzMiIgY29tcGF0IHNlY3Rpb24uCi0tCgpNLmJpdDMyID0ge30gLS0gTHVhIDUuMiAnYml0MzInIGNvbXBhdGliaWxpdHkKCgpsb2NhbCBmdW5jdGlvbiBiaXQzMl9ibm90KHgpCiAgcmV0dXJuICgtMSAtIHgpICUgTU9ECmVuZApNLmJpdDMyLmJub3QgPSBiaXQzMl9ibm90Cgpsb2NhbCBmdW5jdGlvbiBiaXQzMl9ieG9yKGEsIGIsIGMsIC4uLikKICBsb2NhbCB6CiAgaWYgYiB0aGVuCiAgICBhID0gYSAlIE1PRAogICAgYiA9IGIgJSBNT0QKICAgIHogPSBieG9yKGEsIGIpCiAgICBpZiBjIHRoZW4KICAgICAgeiA9IGJpdDMyX2J4b3IoeiwgYywgLi4uKQogICAgZW5kCiAgICByZXR1cm4gegogIGVsc2VpZiBhIHRoZW4KICAgIHJldHVybiBhICUgTU9ECiAgZWxzZQogICAgcmV0dXJuIDAKICBlbmQKZW5kCk0uYml0MzIuYnhvciA9IGJpdDMyX2J4b3IKCmxvY2FsIGZ1bmN0aW9uIGJpdDMyX2JhbmQoYSwgYiwgYywgLi4uKQogIGxvY2FsIHoKICBpZiBiIHRoZW4KICAgIGEgPSBhICUgTU9ECiAgICBiID0gYiAlIE1PRAogICAgeiA9ICgoYStiKSAtIGJ4b3IoYSxiKSkgLyAyCiAgICBpZiBjIHRoZW4KICAgICAgeiA9IGJpdDMyX2JhbmQoeiwgYywgLi4uKQogICAgZW5kCiAgICByZXR1cm4gegogIGVsc2VpZiBhIHRoZW4KICAgIHJldHVybiBhICUgTU9ECiAgZWxzZQogICAgcmV0dXJuIE1PRE0KICBlbmQKZW5kCk0uYml0MzIuYmFuZCA9IGJpdDMyX2JhbmQKCmxvY2FsIGZ1bmN0aW9uIGJpdDMyX2JvcihhLCBiLCBjLCAuLi4pCiAgbG9jYWwgegogIGlmIGIgdGhlbgogICAgYSA9IGEgJSBNT0QKICAgIGIgPSBiICUgTU9ECiAgICB6ID0gTU9ETSAtIGJhbmQoTU9ETSAtIGEsIE1PRE0gLSBiKQogICAgaWYgYyB0aGVuCiAgICAgIHogPSBiaXQzMl9ib3IoeiwgYywgLi4uKQogICAgZW5kCiAgICByZXR1cm4gegogIGVsc2VpZiBhIHRoZW4KICAgIHJldHVybiBhICUgTU9ECiAgZWxzZQogICAgcmV0dXJuIDAKICBlbmQKZW5kCk0uYml0MzIuYm9yID0gYml0MzJfYm9yCgpmdW5jdGlvbiBNLmJpdDMyLmJ0ZXN0KC4uLikKICByZXR1cm4gYml0MzJfYmFuZCguLi4pIH49IDAKZW5kCgpmdW5jdGlvbiBNLmJpdDMyLmxyb3RhdGUoeCwgZGlzcCkKICByZXR1cm4gbHJvdGF0ZSh4ICUgTU9ELCBkaXNwKQplbmQKCmZ1bmN0aW9uIE0uYml0MzIucnJvdGF0ZSh4LCBkaXNwKQogIHJldHVybiBycm90YXRlKHggJSBNT0QsIGRpc3ApCmVuZAoKZnVuY3Rpb24gTS5iaXQzMi5sc2hpZnQoeCxkaXNwKQogIGlmIGRpc3AgPiAzMSBvciBkaXNwIDwgLTMxIHRoZW4gcmV0dXJuIDAgZW5kCiAgcmV0dXJuIGxzaGlmdCh4ICUgTU9ELCBkaXNwKQplbmQKCmZ1bmN0aW9uIE0uYml0MzIucnNoaWZ0KHgsZGlzcCkKICBpZiBkaXNwID4gMzEgb3IgZGlzcCA8IC0zMSB0aGVuIHJldHVybiAwIGVuZAogIHJldHVybiByc2hpZnQoeCAlIE1PRCwgZGlzcCkKZW5kCgpmdW5jdGlvbiBNLmJpdDMyLmFyc2hpZnQoeCxkaXNwKQogIHggPSB4ICUgTU9ECiAgaWYgZGlzcCA+PSAwIHRoZW4KICAgIGlmIGRpc3AgPiAzMSB0aGVuCiAgICAgIHJldHVybiAoeCA+PSAweDgwMDAwMDAwKSBhbmQgTU9ETSBvciAwCiAgICBlbHNlCiAgICAgIGxvY2FsIHogPSByc2hpZnQoeCwgZGlzcCkKICAgICAgaWYgeCA+PSAweDgwMDAwMDAwIHRoZW4geiA9IHogKyBsc2hpZnQoMl5kaXNwLTEsIDMyLWRpc3ApIGVuZAogICAgICByZXR1cm4gegogICAgZW5kCiAgZWxzZQogICAgcmV0dXJuIGxzaGlmdCh4LCAtZGlzcCkKICBlbmQKZW5kCgpmdW5jdGlvbiBNLmJpdDMyLmV4dHJhY3QoeCwgZmllbGQsIC4uLikKICBsb2NhbCB3aWR0aCA9IC4uLiBvciAxCiAgaWYgZmllbGQgPCAwIG9yIGZpZWxkID4gMzEgb3Igd2lkdGggPCAwIG9yIGZpZWxkK3dpZHRoID4gMzIgdGhlbiBlcnJvciAnb3V0IG9mIHJhbmdlJyBlbmQKICB4ID0geCAlIE1PRAogIHJldHVybiBleHRyYWN0KHgsIGZpZWxkLCAuLi4pCmVuZAoKZnVuY3Rpb24gTS5iaXQzMi5yZXBsYWNlKHgsIHYsIGZpZWxkLCAuLi4pCiAgbG9jYWwgd2lkdGggPSAuLi4gb3IgMQogIGlmIGZpZWxkIDwgMCBvciBmaWVsZCA+IDMxIG9yIHdpZHRoIDwgMCBvciBmaWVsZCt3aWR0aCA+IDMyIHRoZW4gZXJyb3IgJ291dCBvZiByYW5nZScgZW5kCiAgeCA9IHggJSBNT0QKICB2ID0gdiAlIE1PRAogIHJldHVybiByZXBsYWNlKHgsIHYsIGZpZWxkLCAuLi4pCmVuZAoKCi0tCi0tIFN0YXJ0IEx1YUJpdE9wICJiaXQiIGNvbXBhdCBzZWN0aW9uLgotLQoKTS5iaXQgPSB7fSAtLSBMdWFCaXRPcCAiYml0IiBjb21wYXRpYmlsaXR5CgpmdW5jdGlvbiBNLmJpdC50b2JpdCh4KQogIHggPSB4ICUgTU9ECiAgaWYgeCA+PSAweDgwMDAwMDAwIHRoZW4geCA9IHggLSBNT0QgZW5kCiAgcmV0dXJuIHgKZW5kCmxvY2FsIGJpdF90b2JpdCA9IE0uYml0LnRvYml0CgpmdW5jdGlvbiBNLmJpdC50b2hleCh4LCAuLi4pCiAgcmV0dXJuIHRvaGV4KHggJSBNT0QsIC4uLikKZW5kCgpmdW5jdGlvbiBNLmJpdC5ibm90KHgpCiAgcmV0dXJuIGJpdF90b2JpdChibm90KHggJSBNT0QpKQplbmQKCmxvY2FsIGZ1bmN0aW9uIGJpdF9ib3IoYSwgYiwgYywgLi4uKQogIGlmIGMgdGhlbgogICAgcmV0dXJuIGJpdF9ib3IoYml0X2JvcihhLCBiKSwgYywgLi4uKQogIGVsc2VpZiBiIHRoZW4KICAgIHJldHVybiBiaXRfdG9iaXQoYm9yKGEgJSBNT0QsIGIgJSBNT0QpKQogIGVsc2UKICAgIHJldHVybiBiaXRfdG9iaXQoYSkKICBlbmQKZW5kCk0uYml0LmJvciA9IGJpdF9ib3IKCmxvY2FsIGZ1bmN0aW9uIGJpdF9iYW5kKGEsIGIsIGMsIC4uLikKICBpZiBjIHRoZW4KICAgIHJldHVybiBiaXRfYmFuZChiaXRfYmFuZChhLCBiKSwgYywgLi4uKQogIGVsc2VpZiBiIHRoZW4KICAgIHJldHVybiBiaXRfdG9iaXQoYmFuZChhICUgTU9ELCBiICUgTU9EKSkKICBlbHNlCiAgICByZXR1cm4gYml0X3RvYml0KGEpCiAgZW5kCmVuZApNLmJpdC5iYW5kID0gYml0X2JhbmQKCmxvY2FsIGZ1bmN0aW9uIGJpdF9ieG9yKGEsIGIsIGMsIC4uLikKICBpZiBjIHRoZW4KICAgIHJldHVybiBiaXRfYnhvcihiaXRfYnhvcihhLCBiKSwgYywgLi4uKQogIGVsc2VpZiBiIHRoZW4KICAgIHJldHVybiBiaXRfdG9iaXQoYnhvcihhICUgTU9ELCBiICUgTU9EKSkKICBlbHNlCiAgICByZXR1cm4gYml0X3RvYml0KGEpCiAgZW5kCmVuZApNLmJpdC5ieG9yID0gYml0X2J4b3IKCmZ1bmN0aW9uIE0uYml0LmxzaGlmdCh4LCBuKQogIHJldHVybiBiaXRfdG9iaXQobHNoaWZ0KHggJSBNT0QsIG4gJSAzMikpCmVuZAoKZnVuY3Rpb24gTS5iaXQucnNoaWZ0KHgsIG4pCiAgcmV0dXJuIGJpdF90b2JpdChyc2hpZnQoeCAlIE1PRCwgbiAlIDMyKSkKZW5kCgpmdW5jdGlvbiBNLmJpdC5hcnNoaWZ0KHgsIG4pCiAgcmV0dXJuIGJpdF90b2JpdChhcnNoaWZ0KHggJSBNT0QsIG4gJSAzMikpCmVuZAoKZnVuY3Rpb24gTS5iaXQucm9sKHgsIG4pCiAgcmV0dXJuIGJpdF90b2JpdChscm90YXRlKHggJSBNT0QsIG4gJSAzMikpCmVuZAoKZnVuY3Rpb24gTS5iaXQucm9yKHgsIG4pCiAgcmV0dXJuIGJpdF90b2JpdChycm90YXRlKHggJSBNT0QsIG4gJSAzMikpCmVuZAoKZnVuY3Rpb24gTS5iaXQuYnN3YXAoeCkKICByZXR1cm4gYml0X3RvYml0KGJzd2FwKHggJSBNT0QpKQplbmQKCnJldHVybiBN"
