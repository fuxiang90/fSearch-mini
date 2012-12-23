#include "../include/CFmmseg.h"

CFmmseg::CFmmseg()
{
    //ctor

    mpath = "~/python/fSearch-mini/fmmseg/";

}

CFmmseg::~CFmmseg()
{
    //dtor
}


void CFmmseg::loadDict()
{
    chdir(mpath.c_str());

    ifstream fin("fmmseg.dic");

    string s;
    int id = 1;
    while(fin>>s){
        mdict.insert(map<string ,int>::value_type(s,id));
        id ++;

        //cout <<s <<endl;
    }


}

bool CFmmseg::isUtfCh(const char ch)
{
     unsigned char start = (unsigned char)ch;

     if(start < (0xC0) ){
        return false;
     }

     return true;
}

void CFmmseg::getChiString( const char *Chi, string &Pointer2Str)
{
    register int i, j;
    int len;
    stringstream ss;

    len = strlen(Chi);

    int flag = isUtfCh( *(Chi + 0) ) ? 1 :0 ;
    for (j = 0, i = 0; i < len; i ++)
    {
        if (isUtfCh( *(Chi + i) ) == true)
        {
            //ss << j++ << ".";
            if(flag ==0)
                ss << " ";
            ss << string(Chi + i, 3) ;
            i +=2;
            flag = 1;
        }
        else {
            if(flag  ) {
                ss << " " ;
            }
            //ss << j++ << ".";
            ss <<string(Chi + i,1) ;

            flag = 0;
        }

    }

    Pointer2Str = ss.str();
}

void CFmmseg::Test()
{
    char *test = "你好hello中国,我是中国人";
    string dest;
    string src;

    loadDict();
    src = test;
    dest = SegmentString( src);
    cout << dest <<endl;

    string in  = "1.in";
    string out = "1.out";
    SegmentFile(in,out);

    //cout << str << endl;
}

bool CFmmseg::firstSegment(const char * chsrc , string & segstr)
{
    getChiString(chsrc,segstr);

    return true;
}

string CFmmseg::SegmentString(string s)
{
    //
    firstSegment(s.c_str() , msrc);

    vector<string> vStr;
    boost::split( vStr, msrc, boost::is_any_of( " " ), boost::token_compress_on );

    for( vector<string>::iterator it = vStr.begin(); it != vStr.end(); ++ it ){
        string  & words = *it ;

        cout << words <<endl;
        if(isUtfCh(words[0]) == true){
            stringstream s2;
            string s1;
            string w;

            s1 = words;

            int start = 0;
            while(s1.size() != 0){
                int len = s1.size();
                if(len > 12){
                    w = s1.substr(0,12);
                }else {
                    w = s1;
                }

                if( isTerm(w)== true ){
                    s2 << " " << w;
                }
                else{
                    string s3;
                    s3  =  w.substr(w.size() - 3,3);
                    w = w.substr(0,w.size() - 3);
                    while(w.size() != 0 ){
                        if(isTerm(w) == true){
                            s3 =  w + " " + s3;
                            break ;
                        }
                        s3 = w.substr(w.size() - 3,3)  + " " + s3;
                        w = w .substr(0,w.size() - 3);
                    }

                    s2 << " " << s3;
                }


                if(len <= 12) {
                    s1  = "";
                }else {
                    s1 = s1.substr(12,len - 12);
                }
            }

            mdest = mdest +s2.str();

        }// end if
        else{
            mdest = mdest + " " + words;
        }
    }




    return mdest;


}

bool CFmmseg::isTerm(string word)
{
    if(mdict.find(word) != mdict.end()){
        return true;
    }
    return false;
}


bool CFmmseg::SegmentFile(string in ,string out)
{
    ifstream fin(in.c_str());
    ofstream fout(out.c_str());

    string s;
    string sout = "";
    while(fin>>s){
        sout = sout +SegmentString(s);
    }
    fout << sout <<endl;

    fin.close();
    fout.close();
}
