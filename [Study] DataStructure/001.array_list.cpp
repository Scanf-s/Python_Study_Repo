#include <iostream>
#include <stream>
#include <algorithm>
using namespace std;

/**
* dynamic array class 정의
*/
template <typename T>
class dynamic_array{
    T data; //Generic type data
    size_t n; //size_t type n

public:
    /**
     * Constructor
     * 배열 크기를 인자로 받은 경우 호출
     * @param n
     */
    dynamic_array(int n){
        this->n = n;
        data = new T[n];
    }

    /**
     * 다른 dynamic_array를 받아서 재생성
     * @param otherArray
     */
    dynamic_array(const dynamic_array<T>& otherArray){
        n = otherArray.n;
        data = new T[n];

        for(int i = 0; i < n; i++){
            data[i] = otherArray[i];
        }
    }

    T& operator[](int index){
        return data[index];
    }

    const T& operator[](int index) const{
        return data[index];
    }

    T& at(int index){
        if (index < n) return data[index];
        throw "Index out of range";
    }

    size_t size() const{
        return n;
    }

    /**
     * array 할당 메모리 소멸자
     */
    ~dynamic_array(){
        delete[] data;
    }

    /**
     * begin() : array의 시작 주소를 반환
     * end() : array의 끝 주소를 반환
     * @return
     */
    T* begin() {
        return data;
    }

    const T* begin() const{
        return data;
    }

    T* end() {
        return data + n;
    }

    const T* end() const {
        return data + n;
    }

    friend dynamic_array<T> operator+(const dynamic_array<T>& arr1, const dynamic_array<T>& arr2){
        dynamic_array<T> resultArray(arr1.size() + arr2.size());
        copy(arr1.begin(), arr1.end(), resultArray.begin());
        copy(arr2.begin(), arr2.end(), resultArray.begin() + arr1.size());

        return resultArray;
    }

    /**
     * @Override
     * to_string 호출 시, 배열의 현재 상태를 출력해줌
     * @param sep
     * @return
     */
    string to_string(const string& sep = ", "){
        if(n == 0) return "";

        ostringstream os;
        os << data[0];

        for(int i = 1; i < n; i++){
            os << sep << data[i];
        }

        return os.str();
    }
};