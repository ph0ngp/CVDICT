# Từ điển Hán Việt CVDICT 

## Giới thiệu
Đây là dự án từ điển Hán Việt được chuyển dịch từ project [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict), với hơn 122000 từ và cụm từ tiếng Trung, bao gồm nhiều cụm từ mới, được sử dụng phổ biến trong ngôn ngữ tiếng Trung hiện đại, mà vốn không có trong các từ điển Hán Việt truyền thống khác.

## Chi tiết
Từng dòng của CVDICT được chuyển dịch từ giải nghĩa tiếng Anh trong CC-CEDICT (chỉ dịch nghĩa, giữ nguyên phần ký tự phồn thể, giản thể và phiên âm pinyin). Phần lớn công việc dịch thuật được thực hiện bởi mô hình ChatGPT-4o đã được fine-tune cho riêng mục đích này. Những dòng dịch sai hoặc nghi ngờ có vấn đề được mình kiểm tra và sửa lại bằng tay, hỗ trợ bởi script.

Khi dịch thuật tự động bằng AI thì không tránh khỏi một xác suất có thể có những lỗi sai khi mô hình bị hallucinate (ảo giác). Tuy mình đã rà soát và sửa lại phần lớn những lỗi đó bằng tay, nhưng không thể tránh khỏi việc vẫn còn sót lỗi. Một số lỗi có thể gặp là:
- Dịch để sót từ tiếng Anh trong nghĩa tiếng Việt (không áp dụng với tên riêng hay thuật ngữ khoa học vì nguyên tắc dịch là giữ nguyên những từ đó).
- Tên của các loài động vật, thực vật hiếm gặp, vì gần như là không có tên tiếng Việt tương đương cho những loài đó. Tuy nhiên, tên khoa học của chúng vẫn được giữ nguyên để đảm bảo độ chính xác.
- Phiên âm Hán Việt của tên riêng tiếng Trung sang tên Hán Việt đôi khi chưa chuẩn xác.
- Cách hành văn đôi khi chưa tự nhiên.
- Một số trường hợp dịch sai nghĩa gốc.

Do đó, các bạn cần lưu ý những điều trên khi sử dụng từ điển này.

## Đóng góp
Nếu bạn thấy có mục nào dịch chưa chuẩn hoặc có ý kiến đóng góp khác, vui lòng tạo pull request hoặc issue trên repo này để mình có thể kiểm tra và sửa lại.

## License
Dự án này được phát hành hoàn toàn miễn phí và phi lợi nhuận bởi tác giả Phong Phan thông qua giấy phép [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/)
