# 파일 입출력1

- 부모클래스의 메소드를 자식이 물려 받았을때 해당 메소드를 자신에 맞게 수정하는 것을 메소드 오버라이딩이라고 한다.
- 부모의 private, static, final메소드는 자식 메소드에서 오버라이딩 할 수 없다.
- 동일한 한 클래스 안에서 이름은 같지만 매개변수의 개수, 순서, 타입의 다른 메소드를 중복해서 정의하는 것을 메소드 오버로딩이라고 한다.
- 메소드 오버로딩은 상속과 무관하다.

# 파일 입출력2

- read() 메소드는 파일에 있는 문자들을 순서대로 읽어서 리턴한다.
- write() 메소드는 해당 문자를 파일에 출력한다.
- 파일을 읽거나 쓸때 파일을 닫는 close() 메소드를 통해 최종적으로 파일을 닫아야 한다.
- FileNotFoundException은 읽고자 하는 파일이 없을 경우 발생하는 exception이다.
- IOException은 입출력에 대한 일반적인 오류 발생시 발생하는 익셉션이다.
- java.io 패키지의 Buffered클래스를 사용하면 필요한 데이터를 미리 한꺼번에 읽어 두거나 모아두었다가 한꺼번에 출력 하는게 가능하다.
