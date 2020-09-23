#!/usr/bin/perl

use strict;

my $param_lines;
while (<ARGV>) {
    $param_lines = $_;
}
# $param_linesの内容はこんな感じ
# param=foo state=present param2=''hoge hoge'' _ansible_check_mode=False _ansible_no_log=False _ansible_debug=False _ansible_diff=False _ansible_verbosity=1 _ansible_version=2.9.10 _ansible_module_name=mymodule _ansible_syslog_facility=LOG_USER _ansible_selinux_special_fs=''[''"''"''fuse''"''"'', ''"''"''nfs''"''"'', ''"''"''vboxsf''"''"'', ''"''"''ramfs''"''"'', ''"''"''9p''"''"'', ''"''"''vfat''"''"'']'' _ansible_string_conversion_action=warn _ansible_socket=None _ansible_shell_executable=/bin/sh _ansible_keep_remote_files=False _ansible_tmpdir=/home/zaki/.ansible/tmp/ansible-tmp-1600577463.6285203-6577-73636997937191/ _ansible_remote_tmp=''~/.ansible/tmp'' 

my $param = getval("param", $param_lines);
my $values = getval("values", $param_lines);
my $dicts = getval("dict", $param_lines);

my $values_str = join(",", map { '"'.$_.'"' } @$values); # string arrayのreferenceを、カンマ区切り・ダブルクォート囲みの文字列変換
my $dicts_str = '{' . join(",", map { '"'.$_.'": ' . '"' . $dicts->{$_} . '"'} keys %$dicts) . '}';

print qq#{"changed": false, "result": "🐰", "param": "$param", "values": [ $values_str ], "dict": $dicts_str}#;
exit 0;

sub getval {
    my $key = shift;
    my $data = shift;

    #return "test";
    if ($data =~ /$key=([^'\s]+)/) {
        # クォートがない単純なやつ
        return $1;
    }
    else {
        if ($data =~ /$key='\[(.*?)\]'/) {
            # list
            my $item = [map { s#'"'"'##g; $_ } split /, /, $1];
            return $item;

            #   values:
            #     - item1
            #     - item2
            #     - item3
            # は、↓になる(連続シングルクォートは実際には1個)
            # values=''[''"''"''item1''"''"'', ''"''"''item2''"''"'', ''"''"''item3''"''"'']''
        }
        if ($data =~ /$key='\{(.*?)\}'/) {
            # dict
            my $item;
            for (map { s#'"'"'##g; $_ } split /, /, $1) {
                my ($k, $v) = split /: /;
                $item->{$k} = $v;
            }
            return $item;
        }
    }

    return "";
}