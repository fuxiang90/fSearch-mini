#ifndef CFMMSEG_H
#define CFMMSEG_H

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <boost/algorithm/string/classification.hpp>
#include <boost/algorithm/string/split.hpp>

using namespace std;
//设计目标 ，
// 输入字符串 or 文件名 ，给出输出，可以位字符串形式 or写入到文本中
class CFmmseg
{

public:
        CFmmseg();
        virtual ~CFmmseg();

        string SegmentString(string s);

        bool SegmentFile(string in ,string out );

        void loadDict();

        void Test();

protected:

private:



    string mpath;
    string msrc;
    string mdest;
    map< string ,int> mdict;


    void getChiString(const char *Chi, string &Pointer2Str);
    bool isUtfCh(const char ch );

    /*分词前的准备 ，做一下简单的分割*/
    bool firstSegment(const char *Chsrc ,string & segstr);
    bool isTerm(string word);

};

#endif // CFMMSEG_H
